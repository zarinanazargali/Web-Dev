from django.urls import path
from api.views import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)

# Lab 10: Generic Views (Level 5 активен)
urlpatterns = [
    # Product endpoints
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/<int:product_id>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # Category endpoints
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view(), name='category-products'),
]

# Lab 9: ViewSet + Router (оставлено для справки)
# from rest_framework.routers import DefaultRouter
# from django.urls import include
# from api.views_lab9 import CategoryViewSet, ProductViewSet
# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
# router.register(r'products', ProductViewSet)
# urlpatterns = [path('', include(router.urls))]
