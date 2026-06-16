from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register_user),
    path('login/', login_user),
    path('', home),

    path('create-complaint/', create_complaint),
    path('view-own-complaints/', view_own_complaints),

    path('manage/complaints/all', view_all_complaints),
    path('manage/complaints/<int:complaint_id>/', update_complaint_status)
    
]