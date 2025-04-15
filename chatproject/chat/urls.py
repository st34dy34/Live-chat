from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import RoomListView, RoomDetailView, RoomCreateView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Přihlášení a odhlášení
    path('login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # Registrace
    path('register/', views.RegisterView.as_view(), name='register'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('rooms/create/', RoomCreateView.as_view(), name='room-create'),
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('rooms/<slug:slug>/', RoomDetailView.as_view(), name='room-detail'),


]
