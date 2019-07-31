from django.db import models
from django.utils import timezone

# Create your models here.
class Switch_set(models.Model):
    set_text =models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.set_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Select(models.Model):
    switch = models.ForeignKey(Switch_set, on_delete=models.CASCADE)
    status_text =models.CharField(max_length=50)
    set =models.IntegerField(default=0)
    def __str__(self):
        return self.status_text

class Test(models.Model):
    test_text = models.CharField(max_length=100)
