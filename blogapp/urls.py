from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
]