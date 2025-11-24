from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        # fields="__all__"
        exclude=['watchlist']
    


class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True , read_only=True)
    # len_name=serializers.SerializerMethodField()
    
    class Meta:
        model=WatchList
        fields="__all__" #We can also define fields individually 
        # fields=['id','name','description']
        # exclude=['active']
        
    # def get_len_name(self,object):
    #     return len(object.name)
    

    # # FIELD LEVEL VALIDATION || We can also use validator for this purpose
    # def validate_name(self,value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is to short!")
    #     else:
    #         return value 
    # #OBJECT LEVEL VALIDATION
    # def validate(self, data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError("NAME AND DESCRIPTION CAN'T Be Same")
    #     return data
    
    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist=WatchListSerializer(many=True,read_only=True)
    # watchlist=serializers.StringRelatedField(many=True) # We can also use HyperLinked Related Field,PrimaryKey Field etc
    # watchlist=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='watch-details')
    
    class Meta:
        model=StreamPlatform
        fields="__all__"
        # extra_kwargs = {
        #     'url': {'view_name': 'stream-details'}
        # }
        

# def Name_Validator(value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         else:
#             return value 
    

# class MovieSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[Name_Validator])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self, validated_data):
#        return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    
#     # FIELD LEVEL VALIDATION || We can also use validator for this purpose
#     # def validate_name(self,value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is to short!")
#     #     else:
#     #         return value 
#     #OBJECT LEVEL VALIDATION
#     def validate(self, data):
#         if data['name']==data['description']:
#             raise serializers.ValidationError("NAME AND DESCRIPTION CAN'T Be Same")
#         return data