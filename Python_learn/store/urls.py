from django.urls import include, path


from . import views

urlpatterns = [
    path('<int:album_id>/', views.detail, name="detail"),  
    path('search/', views.search, name="search"),
    path('', views.list_album, name="list_album"),
]