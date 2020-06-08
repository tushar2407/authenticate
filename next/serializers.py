from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['age', 'bio']

class UserSerializer(serializers.ModelSerializer):
    person=PersonSerializer()
    class Meta:
        model=User
        fields=['pk','username', 'password', 'person']
        extra_kwargs={'password':{'write_only':True, 'required':True }} # to prevent password from showing on api request 
    # to validate post via django rest framework
    # we need to override create user function
    def create(self, validated_data):
        person_data=validated_data.pop('person')
        user=User.objects.create_user(**validated_data) # ** used to convert a dict into kwargs on function call
        user.person=Person.objects.create(user=user,**person_data)
        user.save()
        return user 