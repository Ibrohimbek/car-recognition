from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from recognition.services.car_predictor import CarPredictor


class MainView(View):
    template = 'recognition/main.html'

    def get(self, request):
        return render(request, self.template)

    def post(self, request):
        if not request.FILES.get('photo'):
            return redirect('home')

        photo = request.FILES.get('photo')
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)

        file_path = fs.url(filename)
        result = CarPredictor.predict(f"{settings.BASE_DIR}{file_path}")

        context = {
            'uploaded_file_url': file_path,
            'car_model': result.get('car_model'),
            'probability': result.get('probability')
        }
        return render(request, self.template, context)

