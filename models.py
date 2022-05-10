from django.db import models

# Create your models here
class Article(models.Model):
    title = models.CharField(max_length=500)
    project_img = models.ImageField(upload_to='C:/Users/nina_/Desktop/CodeJango/news/IMAGES/')
    description = models.TextField()
    #date = models.DateField()

    def __str__(self):
        return self.title
