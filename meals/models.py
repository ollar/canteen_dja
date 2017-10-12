from django.db import models


days_choices = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thusday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

category_choices = (
    (0, 'First'),
    (1, 'Second'),
    (2, 'Third'),
    (3, 'Forth'),
)


class Meal(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.IntegerField(default=0, choices=category_choices)
    day_linked = models.IntegerField(default=0, choices=days_choices)
    source_price = models.FloatField(default=0)
    price = models.FloatField(default=0)
    enabled = models.BooleanField(default=True)

    timestamp_created = models.DateTimeField('created', auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
