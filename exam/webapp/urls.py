from django.urls import path
from webapp.views.product import (
        ProductList, 
        ProductDetail, 
        ProductCreate, 
        ProductUpdate, 
        ProductDelete
)
from webapp.views.review import ReviewCreate, ReviewUpdate, ReviewDelete

app_name = 'webapp'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_view'),
    path('product/create/', ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdate.as_view(), name='product_edit'),
    path('product/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('product/<int:pk>/review/create/', ReviewCreate.as_view(), name='review_create'),
    path('review/<int:pk>/edit', ReviewUpdate.as_view(), name='review_edit'),
    path('review/<int:pk>/delete', ReviewDelete.as_view(), name='review_delete')
]