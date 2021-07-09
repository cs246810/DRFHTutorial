from drf_haystack.viewsets import HaystackViewSet, HaystackGenericAPIView
from.models import Note
from .serializers import NoteSerializer


class NoteSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Note]

    serializer_class = NoteSerializer