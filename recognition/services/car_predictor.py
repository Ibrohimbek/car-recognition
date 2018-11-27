from fastai.conv_learner import (
    ConvLearner, tfms_from_model, transforms_side_on, ImageClassifierData, get_cv_idxs, open_image, resnext101_64)
import numpy as np


PATH = "/Users/home/projects/car-recognition/training/data/five_cars/"
sz = 299
arch = resnext101_64
bs = 58
model_name = '5cars299'


class CarPredictor:
    @classmethod
    def predict(cls, photo_path):
        data = cls.get_data()
        learn = ConvLearner.pretrained(arch, data)
        learn.load(model_name)

        trn_tfms, val_tfms = tfms_from_model(arch, sz)
        im = val_tfms(open_image(photo_path))
        preds = learn.predict_array(im[None])
        class_id = np.argmax(preds)
        class_name = learn.data.classes[class_id]
        class_value = preds[0][class_id]
        percentage = round(np.exp(class_value) * 100, 2)
        return {
            'car_model': class_name,
            'probability': percentage
        }

    @staticmethod
    def get_data():
        tfms = tfms_from_model(arch, sz, aug_tfms=transforms_side_on, max_zoom=1.1)

        label_csv = f'{PATH}labels.csv'
        n = len(list(open(label_csv))) - 1
        val_idxs = get_cv_idxs(n)

        data = ImageClassifierData.from_csv(PATH, 'train', f'{PATH}labels.csv',
                                            val_idxs=val_idxs, suffix='.jpg', tfms=tfms, bs=bs)

        return data
