1 - criar ambiente virtual usando o comando: python -m c:\User\Path
2 - ativar o ambiente virtual passando o Path + o script de ativação: \script\activate.bat
3 - instalar o Django(framework python): pip install django
4 - incialize o projeto utilizando o comando: django-admin startproject ou python -m django(caso tenha instalado django via pip)
5 - suba o servidor utilizando o comando: phyton manage.py runserver
6 - importante: utilizar comando Ctrl+Shift+b , digitar python select interpreter, para utilizar a versão Python da venv
7 - inicializar uma app: python manage.py   startapp <nome> 
8 - um projeto pode ter vários app; ou seja, é necessário r
9 - vizuarliazar opções: python manage.py help;
10 - criar arquivo "url.py"; nele, from django.urls import path(para utilizar urls)
11 - from . import views(faz manipulação de qual url queremos devolver p a tela) 
ex: 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
12 - importar > from django.shortcuts import render from django.http import HttpResponse < para a views.py
13 - no url.py se colocará a rota, a view e o name;
14 - na views.py se cria o método da view:
def index(request): 
    return HttpResponse('<h1>manager</h1>')

15 - para redirecionar a url padrão (218.201.12.1) para a desejada (/home)
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/')),
]

16- para habilitar a veiculação de arquivos estáticos durante o desenvolvimento:
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

17- Execute os comandos abaixo para definir as tabelas para aqueles models no banco de dados (verifique se você está no diretório que contém o arquivo manage.py): 
obs: comando utilizado sempre que alterar a estrutura dos dados do banco de dados 

 * python3 manage.py makemigrations > cria as migrações para todos aplicativos instalados em seu projeto
 * python3 manage.py migrate > aplica as migrações em seu banco de dados (Django rastreia quais foram adicionados ao banco de dados atual).