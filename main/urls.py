from rest_framework import routers
from . import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register_new_user/', views.register_new_user),
    path('login_user/', views.login_new_user),
    path('create_post/', views.create_post),
    path('view_post/<int:id>/', views.post_details),
    path('view_post/list/', views.view_post),
    path('user_profile/list/', views.user_profile),
    path('comment/list/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
    path('api-token-auth/', views.login_new_user),
]
