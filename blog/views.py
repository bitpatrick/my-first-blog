from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

#abbiamo creato una funzione chimata post_list che prende request e
#resittuisce --> una funzione "render" che RENDERIZZA (mette insieme)
#il nostro template blog/post_list.html

