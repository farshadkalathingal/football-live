from django.db import models

# Create your models here.
ROUND_CHOICES = [
    ('Round 1', '1'),
    ('Round 2', '2'),
    ('Round 3', '3'),
    ('Pre-Quarter', 'Pre-Qua'),
    ('Quarter', 'Quarter'),
    ('Semi-Final', 'Semi'),
    ('Final', 'Final')
]

class Team(models.Model):
    name = models.CharField(max_length=120, blank=False)
    college = models.TextField()

    def __str__(self):
        return self.name

class Match(models.Model):
    match_num=models.IntegerField()
    round=models.CharField(
        choices=ROUND_CHOICES,
        default='1',
        max_length=30
    )
    t1=models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1")
    t2=models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2")

    def __str__(self):
        return "Match " + str(self.match_num)

class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.CharField(max_length=120)
    goal = models.IntegerField(default=1)


    def __str__(self):
        return self.player