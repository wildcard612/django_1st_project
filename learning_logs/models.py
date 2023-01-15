from django.db import models

class Topic(models.Model):
    ''' User topic'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        ''' model in string'''
        return self.text