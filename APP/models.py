from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    news_details =models.TextField()
    
    def __str__(self) :
        return self.title    