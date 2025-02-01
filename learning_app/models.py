from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    more_info_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
