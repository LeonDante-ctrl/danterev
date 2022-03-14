from django.db import models


class Award(models.Model):
    name=models.CharField(max_length=300)
    description=models.TextField(max_length=5000)     
    developer=models.CharField(max_length=300)
    created_date=models.DateField()
    averangeRating=models.FloatField()
    image=models.URLField(default=None, null=True)
    linktosite=models.URLField(default=None, null=True)


    def __str__(self):
        return self.name

# Create your models here.
