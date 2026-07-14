from rest_framework.viewsets import ModelViewSet
from .models import ProductsModel
from .serailzers import ProductSerializer

class ProductsView(ModelViewSet):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductSerializer