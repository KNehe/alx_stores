from rest_framework.serializers import ModelSerializer
from products.models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "description",]

# testing
# auth & permisions
# ordering, filtering
# docs, pagination, cache, throttling, groups
# image upload to s3
# deploy