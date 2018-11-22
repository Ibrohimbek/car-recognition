from os import listdir
from os.path import isfile, join, isdir, splitext
import shutil
import csv


field_names = ['file_name', 'class']
file_names = []
max_width_or_height = 500


def copy_files():
    for class_name in classes:
        if not isdir(join(path, class_name)):
            continue
        copy_and_rename_files(class_name)

    save_labels_csv()


def copy_and_rename_files(class_name):
    class_path = f"{path}/{class_name}"
    files = [f for f in listdir(class_path) if isfile(join(class_path, f))]

    copy_train_files(class_name, files)


def copy_train_files(class_name, files):
    class_name_ = class_name.replace(' ', '_')

    for counter, file in enumerate(files):
        file_path = f"{path}/{class_name}/{file}"
        file_name, extension = splitext(file)
        if extension not in ['.jpeg', '.jpg']:
            continue

        new_file_name = f'{class_name_}_id_{counter}_{file_name}'
        new_path = f"{join(path, '../train')}/{new_file_name}.jpg"

        shutil.copy(file_path, new_path)

        file_names.append({
            'file_name': new_file_name,
            'class': class_name_,
        })


def save_labels_csv():
    lebels_csv_file = f"{join(path, '../labels.csv')}"
    with open(lebels_csv_file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        writer.writeheader()
        for file_name in file_names:
            writer.writerow(file_name)


def get_new_size(width, height):
    if width > height:
        height = int(height * max_width_or_height / width)
        width = max_width_or_height
    else:
        width = int(width * max_width_or_height / height)
        height = max_width_or_height

    return width, height


if __name__ == "__main__":
    import sys
    if len(sys.argv) is not 2:
        print("Usage: python prepare_photos_to_train.py path_to_folder_with_cars_photos")
    else:
        path = sys.argv[1]
        classes = listdir(path)
        copy_files()
