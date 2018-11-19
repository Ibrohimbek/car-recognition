from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('api/', include('recognition.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
