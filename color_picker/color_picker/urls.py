"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from colors import views
from color_picker import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    # path( 'red_posters', views.red),
    # path( 'yellow_posters/', views.yellow ),
    # path( 'blue_posters', views.blue),
    # path( 'green_posters', views.green),
    # path( 'purple_posters', views.purple),
    # path( 'orange_posters', views.orange),
    # path( 'vermilion_posters', views.vermilion),
    # path( 'amber_poster', views.amber),
    # path( 'chartreuse_poster', views.chartreuse),
    # path( 'teal_poster', views.teal),
    # path( 'violet_poster', views.violet),
    # path( 'magenta_poster', views.magenta),
    # Always leave the index url at the bottom
    path('poster-page.html', views.results),
    path('', views.index),
]
