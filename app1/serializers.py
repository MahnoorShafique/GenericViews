from rest_framework import serializers

from app1.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # creating field not present in model
    # u_name = serializers.SerializerMethodField()
    #
    # def get_f_name(self, obj):
    #     try:
    #         return obj.u_name.f_name
    #     except:
    #         pass
    #
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # author=serializers.CharField(max_length=100)
    # email=serializers.EmailField()
    #
    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Article.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance

    # Using
    # ModelSerializers
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'u_name']
