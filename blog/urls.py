from django.urls import path #importiamo funzione url di django
from . import views #importiamo tutte le nostre views

#possiamo aggiungere il nostro primo modello di URL

urlpatterns = [
    path('', views.post_list,name='post_list'),
    ]
    #stiamo assegnando una
    #view nominata post_list alla URL
    #il "name"  i nome dell'URL che verrà usata per identificare la view
    #è importante dare un nome a ciascuna URL nell'app
    #inoltre dovremmo crcare di mantenere i nomi delle URL unici e facili
    #da ricordare
