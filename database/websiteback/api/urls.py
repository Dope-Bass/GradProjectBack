from .vies import ProjectViewSet, CommentViewSet, MessageViewSet, ParticipantsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'participants', ParticipantsViewSet, basename='participants')
urlpatterns = router.urls

