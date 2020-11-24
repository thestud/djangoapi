from rest_framework import serializers
from .models import Style

class StyleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Style
        fields = ('id', 'url', 'name', 'font', 'fontSize', 'fontColor', 'backgroundColor')
