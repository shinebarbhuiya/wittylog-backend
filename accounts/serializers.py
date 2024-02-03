from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import UserAccount

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_registration',
            'email',
            'profile_picture',
            'device',
            'is_active',
            'last_login',
            # 'is_staff',
            # 'is_superuser',
        )
        read_only_fields = ('id', 'date_of_registration')


    # For custom user registration or update
    def create(self, validated_data):
        # Hash the password before saving it to the database
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserAccountSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password before saving it to the database
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserAccountSerializer, self).update(instance, validated_data)


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('first_name', 'last_name')