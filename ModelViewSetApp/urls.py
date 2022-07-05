from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('modelviewset',views.StudentModelViewSet,basename='modelviewset')
router.register('readonly',views.StudentReadOnlyModelViewSet,basename='readonly')

urlpatterns = [
    path('',include(router.urls)),
]