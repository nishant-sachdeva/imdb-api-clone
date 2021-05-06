from rest_framework import serializers
from watchlist.models import movie

class movieSerializer(serializers.ModelSerializer):
	class Meta:
		model = movie
		# fields=  ['id', 'name', 'description']
		exclude = ['name']

	def validate(self, data):
		if data['name'] == data['description']:
			raise serializers.ValidationError("Title and Desc should be different")
		else:
			return data


	def validate_name(self, value):
		if len(value) < 2:
			raise serializers.ValidationError("Name is too short")
		else:
			return value


# def name_length(value):
# 	if len(value) < 2:
# 		raise serializers.ValidationError("Name is too short!")



# class movieSerializer(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(validators=[name_length])
# 	description = serializers.CharField()
# 	active = serializers.BooleanField()

# 	def create(self, validated_data):
# 		return movie.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		instance.name = validated_data.get('name', instance.name)
# 		instance.description = validated_data.get('description', instance.description)
# 		instance.active = validated_data.get('active', instance.active)
# 		instance.save()

# 		return instance

# 	def validate(self, data):
# 		if data['name'] == data['description']:
# 			raise serializers.ValidationError("Title and Desc should be different")
# 		else:
# 			return data


	# def validate_name(self, value):
	# 	if len(value) < 2:
	# 		raise serializers.ValidationError("Name is too short")
	# 	else:
	# 		return value