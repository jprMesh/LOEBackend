from django.contrib.auth import get_user_model
from rest_framework import serializers
from ratings.models import Prediction, TeamRatingHistory


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['username', 'match', 'predicted_t1_win_prob']


class TeamRatingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRatingHistory
        fields = ['rating', 'rating_index']
        read_only_fields = ['rating', 'rating_index']

class TeamRatingHistoryDateSerializer(serializers.ModelSerializer):
    rating_date = serializers.DateTimeField(source='match.start_timestamp', read_only=True)

    class Meta:
        model = TeamRatingHistory
        fields = ['rating', 'rating_date']
        read_only_fields = ['rating', 'rating_date']
