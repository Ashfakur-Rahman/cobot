from django.db import models

# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def _str_(self):
        return self.name