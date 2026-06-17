from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home),

    path('create-complaint/', create_complaint),
    path('view-own-complaints/', view_own_complaints),

    path('manage/complaints/', view_all_complaints),
    path('manage/complaints/status-update', update_complaint_status)
]