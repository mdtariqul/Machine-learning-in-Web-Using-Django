"""
URL configuration for kmeans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from kmeans import views
from kmeans.views import upload_file
from kmeans.views import upload_data


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.button),
    path('output', views.output , name='script'), 
    path('second/', views.ahre,name='second'),
    path('home/', views.ahree,name='home'),
    path('list/',upload_file, name='list'),
    path('listtt/',upload_data, name='listtt')
    
]
