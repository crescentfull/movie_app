from rest_framework import serilizers
from .models import Movie

class MovieSerializer(serilizers.ModelSerilizer):
    class Meta:
        model = Movie #모델설정
        fields = ('id','title','genre','year')