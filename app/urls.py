from django.urls import path, include
from rest_framework import routers
from .views import NoteSearchView

router = routers.DefaultRouter()
router.register("note/search", NoteSearchView, basename="note-search")

urlpatterns = [
    path('', include(router.urls))
]