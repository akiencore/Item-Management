"""ItemManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from containers.views import home_view, container_detail_view, container_list_view, container_create_view, item_detail_view, item_list_view, item_in_list_view, item_create_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),

    path('containers', container_list_view),
    path('containers/<int:container_id>', container_detail_view),
    path('create-container', container_create_view),


    path('items', item_list_view),
    path('items/in/<int:container_id>', item_in_list_view),
    path('items/<int:item_id>', item_detail_view),
    path('create-item', item_create_view),
]
