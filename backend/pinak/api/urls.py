from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'data', views.DataList, basename='info')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('data/',views.DataList.as_view()),
    path('data/<int:pk>/', views.DataUpdateDelete.as_view()),
    path('data/search/', views.ProductSearchAPIView.as_view(), name='product-search'),
    path('admin/', views.AdminDashboard.as_view(), name='admin_dashboard'),
]