from django.urls import path
from .views import ProductListApiView,ProductListCreateApiView, ProductListMixedUpdateApiView,ProductDetailApiView,ProductDeleteApiView,ProductUpdateApiView

urlpatterns=[
    path('productlar/', ProductListApiView.as_view()),
    path('product/create/', ProductListCreateApiView.as_view() ),
    path('product/mixedupdate/<int:pk>', ProductListMixedUpdateApiView.as_view()),
    path('product/detail/<int:pk>', ProductDetailApiView),
    path('product/delete/<int:pk>', ProductDeleteApiView),
    path('product/update/<int:pk>', ProductUpdateApiView)
]