from django.urls import path

from .views import artiste_list_api, artiste_detail_api

urlpatterns = [ 
    path('songcrud/', artiste_list_api, name='artiste_list_api'),
    path('songcrud/<int:id>/', artiste_detail_api, name='artiste_detail_api'),
]