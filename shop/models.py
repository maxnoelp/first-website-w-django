from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kunde(models.Model):
    benutzer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
    
class Artikel(models.Model):
    name=models.CharField(max_length=200, null=True)
    beschreibung=models.TextField(blank=True, null=True)
    preis=models.FloatField()

    def __str__(self):
        return self.name
    
class bestellung(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    bestelldatum = models.DateTimeField(auto_now_add=True)
    erledigt = models.BooleanField(default=False, null=True, blank=True)
    auftragsId = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class bestellteArtikel(models.Model):
    artikel = models.ForeignKey(Artikel, on_delete=models.SET_NULL, null=True, blank=True)
    Bestellung = models.ForeignKey(bestellung, on_delete=models.SET_NULL, null=True, blank=True)
    menge = models.IntegerField(default=0, null=True, blank=True)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artikel.name
    
class Adresse(models.Model):
    kunde = models.ForeignKey(Kunde, on_delete=models.SET_NULL, null=True, blank=True)
    Bestellung = models.ForeignKey(bestellung, on_delete=models.SET_NULL, null=True, blank=True)
    adresse=models.CharField(max_length=200, null=True)
    plz=models.CharField(max_length=200, null=True)
    stadt=models.CharField(max_length=200, null=True)
    land=models.CharField(max_length=200, null=True)
    datum = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.adresse