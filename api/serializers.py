from rest_framework import serializers
from .models import MyUser,Blog,Comments

class MyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ["name","email","password"]

    def create(self, validated_data):

        user = MyUser.objects.create(email = validated_data['email'],name = validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class loginuserSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length = 250)
    password = serializers.CharField(max_length = None)



class BlogSerializer(serializers.ModelSerializer):
    likes = serializers.IntegerField(default=0, read_only=True,source = "likes.count")
    author = serializers.EmailField( read_only=True,source = "author.email")

    class Meta:
        model = Blog
        fields = ['id','title','content','author',"published_date",'updated_date','likes','is_deleted']
  
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance
 



class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(read_only=True, source='owner.email')
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        fields = ['id', 'blog', 'owner', 'content', 'created_date', 'replies']

    def get_replies(self, obj):
        replies = Comments.objects.filter(parent_comment = obj.id)
    
        return CommentSerializer(replies, many=True).data
    def create(self, validated_data):
        # Remove the 'blog' field from validated data as it is not a valid argument to create a new comment
        validated_data.pop('reply-to', None)

        # Create the new comment object
        comment = Comments.objects.create(**validated_data)

        return comment
