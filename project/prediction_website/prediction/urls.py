from django.urls import path
from . import views

app_name = 'prediction'
urlpatterns = [
    path('', views.upload_file, name='upload'),  # Root URL pattern
    path('result/<int:upload_id>/', views.result, name='result'),
]
