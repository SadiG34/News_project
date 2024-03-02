from django.urls import path

from web.views import *

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path('news/add', news_edit_view, name='news_add'),
    path('news/<int:id>/edit', news_edit_view, name='news_edit'),
    path('news/<int:id>/', news_commentaries, name='commentaries_add'),
    path('news/<int:id>/delete/', news_delete_view, name='news_delete'),
    path('tags/', tags_view, name='tags'),
    path('add_to_favorites/<int:news_id>/', add_to_favorites, name='add_to_favorites'),
    path('tags/<int:id>/delete/', tags_delete_view, name='tags_delete'),
    path('add_user/', add_user_view, name='add_user'),
    path('delete_user/<int:id>/delete', remove_user_view, name='delete_user'),
    path('settings/', settings, name='settings'),
    path('block_user/', block_user, name='block_user')
]

