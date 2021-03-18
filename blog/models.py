from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model): #models.Model sta a indicare che il post
    #è un modello Django, quindi Django sa che dovrebbe essere salvato
    #nel DB
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #questa è una relazione per ogni istanza della classe post a un
    #altro singolo oggetto
    title = models.CharField(max_length=200)
    #cosi si definisce un testo con un numero limitato di lettere
    text = models.TextField()
    #cosi si definisce un testo senza un limite
    created_date = models.DateTimeField(default=timezone.now)
    #questo per la data ed l'ora
    published_date = models.DateTimeField(blank=True,null=True)
    #questo è un link a un altro modello

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
