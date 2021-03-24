#vogliamo usare 127 come homepage per il nostro blog e
#visualizzare elenco post

#vogliamo mantenere il file di mysite/urls.py pulito, quindi importeremo
#le url dalla nostra applicazione "blog" sul file principale
# " mysite/urls.py "


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')), #sto dicendo se vado nella home
    #page allora manda la stringa restante e urlconf = blog.urls
]
