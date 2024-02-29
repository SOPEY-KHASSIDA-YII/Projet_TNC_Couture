from django.shortcuts import render
from TNC.models import Mesure,Commande
from TNC.froms import ContactUsForm, MesureForm, CommandeForm
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def mesure(request): 
    mesures = Mesure.objects.all()
    return render(request,
                  'TNC/mesure_liste.html',
                  {"mesures":mesures}
                  )
    
def mesure_detail(request, id):  # notez le paramètre id supplémentaire
    mesures = Mesure.objects.get(id=id)
    return render(request,
                    'TNC/mesure_detail.html',
                    {'mesures':mesures}) 
    
def mesure_create(request):
    if request.method == "POST":
        form = MesureForm(request.POST)
        if form.is_valid:
            mesure = form.save()            
        return redirect("mesure-detail",mesure.id)
    else : 
        form = MesureForm()        
    return render(request,
                  'TNC/mesure_create.html',
                  {'form': form}
                  )
    
def mesure_update(request, id):
    mesure = Mesure.objects.get(id=id)
    if request.method == "POST":
        form = MesureForm(request.POST, instance=mesure)
        if form.is_valid:
            mesure = form.save()
        return redirect("mesure-detail", mesure.id)
    else:
        form = MesureForm(instance=mesure)
    return render(request,
                  'TNC/mesure_update.html',
                  {'form': form}
                  )

def mesure_delete(request, id):
    mesure = Mesure.objects.get(id=id)
    if request.method == 'POST':
        mesure.delete()
        return redirect('mesure-liste')
    return render(request,
           'TNC/mesure_delete.html',
           {'mesure': mesure})

def commande(request): 
    commandes = Commande.objects.all()
    return render(request,
                  'TNC/commande_liste.html',
                  {"commande":commandes}
                  )  
    
def commande_detail(request, id):
    commandes = Commande.objects.get(id=id)
 
    return render(request,
                    'TNC/commande_detail.html',
                    {'commande':commandes}
                    )

def commande_create(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid:
            commande = form.save()
        return redirect('commande-detail',commande.id)
    else:
        form = CommandeForm()
    return render(request, 
                  'TNC/commande_create.html',
                  {'form':form})
    
def commande_update(request, id):
    commandes = Commande.objects.get(id=id)
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commandes)
        if form.is_valid:
            commandes = form.save()
        return redirect('commande-detail',commande.id)
    else:
        form = CommandeForm(instance=commandes)
    return render(request,
                  'TNC/commande_update.html',
                  {'form':form})
 
def contact(request): 
    if request.method == "POST" : 
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via TNC Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@tnc.xyz'],
                )
            return redirect('/contact/')
    else:
        form =ContactUsForm()
    return render(request,
                  'TNC/contact.html',
                  {"form":form}
                  )
