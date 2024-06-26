from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('results/', views.results_view, name='results_view'),
    path('upload-form/', views.upload_form_view, name='upload_form'),
    path('api/stockdata/<str:ticker>/', views.StockDataView.as_view(), name='stock-data'),
    path('batch-upload/', views.batch_upload, name='batch_upload'),
]
