from rest_framework import serializers

from .models import Todo
#add your code here
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)