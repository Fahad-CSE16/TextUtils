
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='Analyze'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),

]
"""path('capitalizedfirst', views.capitalizedfirst, name='capitalizedfirst'),
    path('newlinermv', views.newlinermv, name='newlinermv'),
    path('spacermv', views.spacermv, name='spacermv'),
    path('Charcount', views.Charcount, name='Charcount')"""