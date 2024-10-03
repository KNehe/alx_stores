from rest_framework.routers import DefaultRouter
from api.products.views import ProductViewSet, products_list
from django.urls import path



router = DefaultRouter()
router.register('', ProductViewSet, basename='product')



urlpatterns = [
    path('v2_list/', products_list, name='product_list'),
]
urlpatterns += router.urls