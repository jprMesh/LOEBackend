from django.db import models
from django.conf import settings
from colorfield.fields import ColorField


class Team(models.Model):
    LEAGUE_REGIONS = [
        ('NA', 'North America'),
        ('EU', 'Europe'),
        ('KR', 'Korea'),
        ('CN', 'China'),
        ('INT', 'International')
    ]

    # team_id pk
    team_continuity_id = models.IntegerField()
    team_name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=5)
    region = models.CharField(max_length=3,
        choices=LEAGUE_REGIONS)
    color1 = ColorField()
    color2 = ColorField()
    logo_img = models.URLField()

    def __str__(self):
        return self.team_name


class Match(models.Model):
    # match_id pk
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='side1_match')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='side2_match')
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    match_datetime = models.DateTimeField()

    def __str__(self):
        return f'{str(self.team1)} vs {str(self.team2)} -- {str(self.match_datetime)}'


class TeamRating(models.Model):
    # teamrating_id pk
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rating_date = models.DateTimeField()
    rating = models.IntegerField()

    def __str__(self):
        return f'{self.team}: {str(self.rating_date)}'


class Prediction(models.Model):
    # prediction_id pk
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    predicted_t1_win_prob = models.IntegerField()

    def __str__(self):
        return f'{self.user}--{str(self.match)}: {str(self.predicted_t1_win_prob)}'


class UserScore(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {str(self.score)} -- {str(self.score_updated)}'
