from __future__ import unicode_literals
from ..login.models import User
from django.db import models
# from datetime import datetime
import datetime

# Create your models here.
class TripManager(models.Manager):
    # trip creation
    def trip_creator(self, postData, current_user):
        trip = self.create(
        destination = postData['destination'],
        description = postData['description'],
        travelDateFrom = postData['travelDateFrom'],
        travelDateTo = postData['travelDateTo'],
        planner = User.objects.get(id=current_user.id)       
        )
        # print trip
        return trip
    # trip validation
    def trip_validator(self, postData):
        results = {
            'status': True,
            'errors': []
            }
        # validation for empty entries
        if len( postData['destination']) < 1:
            results['status'] = False
            results['errors'].append("no empty entries")
        # validation for minimum characters
        if len( postData['description']) < 1:
            results['status'] = False
            results['errors'].append("no empty entries")
        # travel dates validation
        now = datetime.datetime.now()
        travelStartDate = datetime.datetime.strptime(postData['travelDateFrom'], '%m/%d/%Y') 
        travelEndDate = datetime.datetime.strptime(postData['travelDateTo'], '%m/%d/%Y') 
        # checking if entry if beyond Today!!!
        if (travelStartDate <= now) or (travelEndDate <= now):
            results['status'] = False
            results['errors'].append("Travel Dates should always be in the future!!") 
        # Travel Date To greater than Travel Date From      
        if travelStartDate > travelEndDate:
            results['status'] = False
            results['errors'].append("Travel Date To should not be before Travel Date From!!")
        # pass
        return results

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255) 
    travelDateFrom = models.CharField(max_length=255)
    travelDateTo = models.CharField(max_length=255)    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    planner = models.ForeignKey(User, related_name = 'plannedTrips')
    travelers = models.ManyToManyField(User, related_name ='allTrips')
    objects = TripManager()

    def __repr__(self):
        return "<Trip object: {} {}>".format(self.destination, self.description, self.planner)