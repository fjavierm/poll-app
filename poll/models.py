from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    choice_1 = models.CharField(max_length=30)
    choice_2 = models.CharField(max_length=30)
    choice_3 = models.CharField(max_length=30)
    choice_1_count = models.IntegerField(default=0)
    choice_2_count = models.IntegerField(default=0)
    choice_3_count = models.IntegerField(default=0)

    def total(self):
        return self.choice_1_count + self.choice_2_count + self.choice_3_count
