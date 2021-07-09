from drf_haystack.serializers import HaystackSerializer
from .search_indexes import NoteIndex


class NoteSerializer(HaystackSerializer):

    class Meta:
        index_classes = [NoteIndex]

        fields = ['text', 'author', 'pub_date']