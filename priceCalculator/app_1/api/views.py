from app_1.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from app_1.api.serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)