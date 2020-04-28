from rest_framework import serializers

from ..models import Project, Comment, Message, Participant


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'founder', 'start_date', 'end_date', 'check_date', 'design', 'functional',
                  'discussion', 'idea', 'bug', 'not_formal', 'description', 'stage')


class CommentForm(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'project', 'founder', 'date', 'text')


class MessageForm(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'receiver', 'sender', 'text', 'date', 'title')


class ParticipantForm(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ('user_name', 'project')
