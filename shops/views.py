# shops/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from math import radians, sin, cos, sqrt, atan2

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        user_lat = float(request.query_params.get('latitude', 0))
        user_lon = float(request.query_params.get('longitude', 0))

        shops = Shop.objects.all()
        shop_distances = []

        for shop in shops:
            distance = self.calculate_distance(user_lat, user_lon, shop.latitude, shop.longitude)
            shop_distances.append((shop, distance))

        shop_distances.sort(key=lambda x: x[1])
        sorted_shops = [shop for shop, _ in shop_distances]

        serializer = self.get_serializer(sorted_shops, many=True)
        return Response(serializer.data)

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371  # Earth's radius in kilometers

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c

        return distance