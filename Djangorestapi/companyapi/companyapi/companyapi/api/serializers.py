from rest_framework import serializers
from api.models import Company


#create serializers here

class Companyserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
