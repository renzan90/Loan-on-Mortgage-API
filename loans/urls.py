from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('loans', LoanViewSet, basename='loans')

urlpatterns = [

]

urlpatterns += router.urls