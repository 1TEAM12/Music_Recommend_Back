from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlaylistView.as_view(), name='playlist_view'),
    path('<int:playlist_id>/', views.PlaylistDetailView.as_view(), name='playlist_detail_view'),
    path('<int:playlist_id>/<int:song_id>/', views.PlaylistSongView.as_view(), name='playlist_song_view'),
]
