from rest_framework.serializers import ModelSerializer
from api.models import MeetUp

class MeetUpSerializer(ModelSerializer):
    class Meta:
        model = MeetUp
        fields = '__all__'
