from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views import View


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

        context = {
            'uploaded_file_url': fs.url(filename)
        }
        return render(request, self.template, context)
