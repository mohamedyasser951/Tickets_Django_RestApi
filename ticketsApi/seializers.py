from rest_framework import routers, serializers, viewsets
from .models import Guest,Movie,Reservations
# Guest movie reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = "__all__"

class GuestSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ["pk","reservation","name","phone"]