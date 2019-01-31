from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # path('hello-view/', views.HelloApiView.as_view())
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]
