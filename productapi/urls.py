from django.urls import path
from .views import ProductListApiView,ProductListCreateApiView, ProductMixedApiView,ProductDetailApiView,ProductDeleteApiView,ProductUpdateApiView

urlpatterns=[
    path('productlar/', ProductListApiView.as_view()),
    path('product/create/', ProductListCreateApiView.as_view() ),
    path('product/mixed/<int:pk>/', ProductMixedApiView.as_view()),
    path('product/<int:pk>/', ProductDetailApiView.as_view()),
    path('product/delete/<int:pk>/', ProductDeleteApiView.as_view()),
    path('product/update/<int:pk>/', ProductUpdateApiView.as_view())
]