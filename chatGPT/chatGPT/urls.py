"""chatGPT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from .views import chatGPT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',chatGPT,name="chatGPT"),
    path('gptApp/',include('gptApp.urls')),
]


#python.exe -m pip install --upgrade openai
#python.exe -m pip install python-dotenv    to be able to read the openai key
#python.exe -m pip install --upgrade pip
#pip install djongo



