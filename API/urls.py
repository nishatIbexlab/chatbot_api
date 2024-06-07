"""
URL configuration for creatego project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import assistant, project_list, get_chat_history, upload_chat_history, upload_group_thread

urlpatterns = [
    path("", assistant.as_view(), name="index"),   
    path("projects/", project_list, name="project_list"),
    path("chat/", get_chat_history, name="supabase_test"),    
    path("upload/", upload_chat_history, name="upload_chat_history"),
    path("add/", upload_group_thread, name="adding member to group chat"),
    
]
