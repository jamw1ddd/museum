from django.urls import path
from .views import home,about,contact_view,membership,gallery

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact_view, name='contact'),
    path('membership/', membership, name='membership'),
    path('gallery/', gallery, name='gallery'),
]