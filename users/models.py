from django.db import models


class User(models.Model):
    real_name = models.CharField(max_length=200)
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    timestamp_created = models.DateTimeField(auto_now_add=True)
    timestamp_modified = models.DateTimeField(auto_now=True)

    # orders = relationship('Order', backref='user')

    def __str__(self):
        return '{} ({})'.format(self.real_name, self.username)

    timestamp_created.admin_order_field = 'timestamp_created'
    timestamp_created.short_description = 'created'
