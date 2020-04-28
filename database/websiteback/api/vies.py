from ..models import Project, Comment, Message, Participant
from .serializers import ProjectSerializer, CommentForm, MessageForm, ParticipantForm

from rest_framework import viewsets


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentForm
    queryset = Comment.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageForm
    queryset = Message.objects.all()


class ParticipantsViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipantForm
    queryset = Participant.objects.all()