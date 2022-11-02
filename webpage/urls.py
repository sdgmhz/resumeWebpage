
from django.urls import path
from webpage.views import *

app_name = 'webpage'

urlpatterns = [
    path('', index_view, name='index'),
    path('profile', profile_view, name='profile'),
    path('education', education_view, name='education'),
    path('languages', languages_view, name='languages'),
    path('projects', projects_view, name='projects'),
    path('skills', skills_view, name='skills'),
    path('contact', contact_view, name='contact'),
]
