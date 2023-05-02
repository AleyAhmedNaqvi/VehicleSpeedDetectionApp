from django.db import models

class Video(models.Model):
  caption=models.CharField(max_length=100)
  video=models.FileField(upload_to="videos/",null=True,verbose_name="")
  def __str__(self):
    return self.caption + ": " + str(self.video)
# Create your models here.
