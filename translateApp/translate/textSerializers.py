from rest_framework import serializers
from translate.models import Text

# Test Serializer - serializes translated and untranslated texts
class TextSerializer(serializers.ModelSerializer):
  class Meta:
    model = Text 
    fields = '__all__'