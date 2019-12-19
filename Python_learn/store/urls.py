from django.urls import include, path


from . import views

urlpatterns = [
    path('<int:album_id>/', views.detail),  
    path('search/', views.search),
    path('', views.list_album),
]