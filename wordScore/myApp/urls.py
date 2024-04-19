# urls.py

from django.urls import path
from . import views
from .views import back_or_default

urlpatterns = [
    path('Scan-Result', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    path('keyword-scan/', views.keyword_scan, name='keyword_scan'),
    path('user-files/', views.user_files, name='user_files'),
    
    path('file-details/<int:file_id>/', views.file_details, name='file_details'),
    path('back/', back_or_default, name='back'),
    path('senti/', views.user_upload, name='user_upload'),
    path('', views.test, name='test'),
    path('Profile/', views.Profile, name='Profile'),
    path('backUp/', views.backUp, name="backUp"),
    
    path('restore_file/<int:file_id>/', views.restore_file, name='restore_file'),
    path('restore_files/<int:file_id>/', views.restore_files, name='restore_files'),

    path('move_file/<int:file_id>/', views.move_file, name='move_file'),
    path('move_fileKey/<int:file_id>/', views.move_fileKey, name='move_fileKey'),

    path('delete-file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete-files/<int:file_id>/', views.delete_files, name='delete_files'),
]
