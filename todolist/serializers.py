from rest_framework import serializers

from .models import Todo, Subject, Exam

class SubjectSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Subject
        fields = '__all__'
        
class TodoSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Todo
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['subject'] = SubjectSerializer(read_only=True)
        return super(TodoSerializer, self).to_representation(instance)

class ExamSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Exam
        fields = '__all__'
    
    def to_representation(self, instance):
        self.fields['subject'] = SubjectSerializer(read_only=True)
        return super(ExamSerializer, self).to_representation(instance)