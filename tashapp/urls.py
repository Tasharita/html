
from django.contrib import admin
from django.urls import path
from tashapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('form/', views.form,name='form'),
]
