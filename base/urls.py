from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.loginPage, name="Login"),
    path('logout/', views.logoutUser, name="logout"),
     path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),

    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
     path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),

]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)