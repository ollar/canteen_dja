from django.db import models


class Meal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.IntegerField()
    day_linked = models.IntegerField()
    source_price = models.FloatField(null=False)
    price = models.FloatField(null=False)
    enabled = models.BooleanField(default=True)

    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
