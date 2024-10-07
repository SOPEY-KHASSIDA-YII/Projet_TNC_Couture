from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Mesure(models.Model):
    def __str__(self):
        return f'{self.prenom} {self.nom}'
    
    class Genre(models.TextChoices):
        Homme = "H"
        Femme = "F"
    nom = models.fields.CharField(max_length = 50)
    prenom = models.fields.CharField(max_length = 50)
    tel = models.fields.IntegerField()
    genre = models.fields.CharField(choices = Genre.choices, max_length = 5)
    year = models.fields.IntegerField(
        validators = [MinValueValidator(1900),MaxValueValidator(2021)])
    page_officielle = models.fields.URLField(null = True, blank = True)
    active = models.fields.BooleanField(default = True)
    epaule = models.fields.IntegerField()
    longueur_bb= models.fields.IntegerField()
    coup = models.fields.IntegerField()
    bras = models.fields.IntegerField()
    longueur_pt = models.fields.IntegerField()
    
class Commande(models.Model):

    type = models.fields.CharField(max_length = 50)
    mesure = models.ForeignKey(Mesure,null = True,on_delete = models.SET_NULL)
    

    

    


