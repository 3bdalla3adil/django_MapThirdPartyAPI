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
    origins = TransientModel.TextField("Origins")
    destination = TransientModel.TextField("destination")
    destinations = TransientModel.TextField("destinations")
    
    q = TransientModel.TextField("q")
    gl = TransientModel.TextField("gl")
    hl = TransientModel.TextField("hl")
    autocorrect = TransientModel.Boolean("autocorrect")