from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('News', views.news, name='News'),
    path('contact', views.contact, name='contact'),
    path('my', views.my, name='my'),
    path('why', views.why, name='why'),
    path('login', views.login_user, name='login'),
]


