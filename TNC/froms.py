from django import forms
from TNC.models import Mesure,Commande

class ContactUsForm(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
    
class MesureForm(forms.ModelForm):
   class Meta:
      model = Mesure
      # fields = '__all__'
      exclude = ('active', 'page_officielle')
      
class CommandeForm(forms.ModelForm):
    class Meta :
        model = Commande
        fields = '__all__'