from django.urls import path
from django.contrib import admin

from trackhours.views import privacy, terms, plans, frontpage
from userprofile.views import signup

app_name = 'trackhours'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('privacy/', privacy, name='privacy'),
    path('terms/', terms, name='terms'),
    path('plans/', plans, name='plans'),
    
    #
    # Auth
    path('signup/', signup, name='signup'),
]

