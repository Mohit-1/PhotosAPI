from rest_framework import serializers
from photos.models import Photo, Group

class PhotoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Photo
		fields = ('pid', )

class PhotoDataSerializer(serializers.ModelSerializer):
	group = serializers.StringRelatedField() #group was serialized by its pk, eg -1,2 etc. 
											#This makes group display the __str__ instead.

	class Meta:
		model = Photo
		fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = '__all__'