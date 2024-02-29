from django.contrib import admin
from TNC.models import Mesure
from TNC.models import Commande

# Register your models here.
class MesureAdmin(admin.ModelAdmin): 
    list_display = ('nom','prenom','year', 'genre') 
class CommandeAdmin(admin.ModelAdmin):
     list_display = ('type','mesure')
     
admin.site.register(Mesure,MesureAdmin)
admin.site.register(Commande,CommandeAdmin)
