from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/', views.temp, name='temp'),
    path('dresses/', views.dresses, name='dresses'),
    path('gymwear/', views.gymwear, name='gymwear'),
    path('jackets/', views.jackets, name='jackets'),
    path('jeans/', views.jeans, name='jeans'),
    path('shirts/', views.shirts, name='shirts'),
    path('shoes/', views.shoes, name='shoes'),
    path('contact/', views.contact, name='contact'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
