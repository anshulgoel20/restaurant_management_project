"""
WSGI config for restaurant_management project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')

application = get_wsgi_application()
from django.conf import settings
from django.shortcuts import render

def home(request)
  restaurant_management=settings.restaurant_name

  import django.shortcuts import render

  def menu_list(request)
   header h1{
    margin:0;
    font-size:2.5rem;
   }

   def contact_us(request):
    contact_info={
        "address":"123 food certificate"
    }