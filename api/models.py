from django.db import models

# Create your models here.
class TransientModel(models.Model):
    def save(*args,**kwargs):
        pass
    class Meta:
        abstract = True
        managed = False

class ThirdPartyAPI(TransientModel):
    origin = TransientModel.TextField("Origin")