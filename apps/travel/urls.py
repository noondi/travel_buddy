from django.conf.urls import url
from . import views




urlpatterns = [  
    url(r'^travels$', views.home),
    url(r'^travels/add$', views.planAdd),
    url(r'^travels/tripAdd$', views.tripAdd),
    url(r'^travels/showAttack$', views.showAttack),
    url(r'^travels/destination/(?P<trip_id>\d+)$', views.showDestination),
    url(r'^travels/join/(?P<trip_id>\d+)$', views.joinTrip),
    # url(r'^home$', views.home),
    # url(r'^logout$', views.logout),
]
