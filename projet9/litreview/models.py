from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=128)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'titre: {} description : {} date :{}'.format(self.title, self.description, self.time_created)


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following_by')

    class Meta:
        unique_together = ['user', 'followed_user']

    def __str__(self):
        return 'personne follow {} suivi par {}'.format(self.user, self.followed_user)


class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    answer_review = models.BooleanField(default=False)


    def __str__(self):
        return 'ticket {} rating {} user {} headline {} body {} timecreated {} ' \
               'answer_review {}'.format(self.ticket, self.rating, self.user, self.headline,
                                         self.body, self.time_created, self.answer_review)
