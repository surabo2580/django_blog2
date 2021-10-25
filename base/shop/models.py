from django.db import models

# Create your models here.
class News_Post(models.Model):
    sno = models.AutoField(primary_key=True)
    headlines = models.CharField(max_length=200)
    content = models.TextField()
    source = models.CharField(max_length=200)
    slug = models.CharField(max_length=140)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.headlines + 'by' + self.source
