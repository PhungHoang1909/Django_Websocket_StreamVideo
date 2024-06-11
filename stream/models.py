from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VideoLink(models.Model):
    url = models.CharField(max_length=255)
    group = models.ForeignKey(Group, related_name='videos', on_delete=models.CASCADE)

    def __str__(self):
        return self.url
