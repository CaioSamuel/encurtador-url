import string, random
from django.shortcuts import render, get_object_or_404, redirect
from .models import URL

# Create your views here.

def gerar_codigo():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

def encurtar(request):
    if request.method == 'POST':
        url_original = request.POST.get('url_original')
        codigo_curto = gerar_codigo()

        novo_registro = URL(url_original=url_original, codigo_curto=codigo_curto)
        novo_registro.save()

        return render(request, 'urls/resultado.html', {'codigo': codigo_curto})
    return render(request,  'urls/index.html')

def redirecionar(request, codigo_curto):
    url_obj = get_object_or_404(URL, codigo_curto=codigo_curto)
    return redirect(url_obj.url_original)