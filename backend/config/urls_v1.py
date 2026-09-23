from django.urls import include, path

from llm.views import (
    ChatFinalizeView,
    ChatMessageView,
    ChatRoomDetailView,
    ChatRoomView,
    ChatTurnListView,
    GuestChatView,
)


urlpatterns = [
    path("", include("travel.urls")),
    path("community/", include("community.urls")),
    path("chat/sessions/", ChatRoomView.as_view()),
    path("chat/sessions/<int:session_id>/", ChatRoomDetailView.as_view()),
    path("chat/sessions/<int:session_id>/messages/", ChatMessageView.as_view()),
    path("chat/sessions/<int:session_id>/turns/", ChatTurnListView.as_view()),
    path("chat/turns/<uuid:turn_id>/finalize/", ChatFinalizeView.as_view()),
    path("chat/guest/", GuestChatView.as_view()),
    path("auth/", include("accounts.urls")),
    path("baseball/", include("baseball.urls")),
    path("tving/", include("tving.urls")),
]