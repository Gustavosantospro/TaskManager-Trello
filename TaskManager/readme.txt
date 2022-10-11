1 - criar ambiente virtual usando o comando: python -m c:\User\Path
2 - ativar o ambiente virtual passando o Path + o script de ativação: \script\activate.bat
3 - instalar o Django(framework python): pip install django
4 - incialize o projeto utilizando o comando: django-admin startproject ou python -m django(caso tenha instalado django via pip)
5 - suba o servidor utilizando o comando: phyton manage.py runserver
6 - importante: utilizar comando Ctrl+Shift+b , digitar python select interpreter, para utilizar a versão Python da venv
7 - inicializar uma app: python manage.py   startapp <nome> 
8 - um projeto pode ter vários app; ou seja, é necessário registrar: pegar o nome da subclasse appConfig, em 
- apps.py; depois só colar esse nome em INSTALLED_APPS ; 
9 - vizuarliazar opções: python manage.py help;
10 - criar arquivo "url.py"; nele, from django.urls import path(para utilizar urls)
11 - from . import views(faz manipulação de qual url queremos devolver p a tela) 
ex: 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]