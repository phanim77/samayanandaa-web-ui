"""samayanandaa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.conf.urls import include, url
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from samayanandaa_web import views
#urlpatterns = [
#    url(
#        regex=r'$', 
#       view=views.index, 
#        name='home'
#    ),
#        url(
#        regex=r'$', 
#        view=views.payment, 
#        name='payment'
#    ),
#    url(r'^', include('samayanandaa_web.urls')),
#]

router = routers.DefaultRouter()
router.register(r'feedback_api', views.FeedbackView, 'feedback')

urlpatterns = [
    path('', views.index, name='home'),
    path('payment', views.payment, name='payment'),
    path('feedback', views.feedback, name='feedback'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('admin', admin.site.urls),
    path('api/', include(router.urls))
]
