from rest_framework import serializers
from .models import Contact,MapUserContact,Profile
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
