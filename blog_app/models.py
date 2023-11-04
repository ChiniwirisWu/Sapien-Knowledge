from django.db import models

# Create your models here.
class Page(models.Model):
    content = models.CharField(max_length=2000)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100, default="none")
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
