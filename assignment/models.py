from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Incident(models.Model):
    location = models.CharField(max_length=100)
    incident_department = models.CharField(max_length=100)
    incident_date = models.DateField()
    incident_time = models.TimeField()
    incident_location = models.CharField(max_length=100)
    initial_severity = models.CharField(max_length=100)
    suspected_cause = models.CharField(max_length=100)
    immediate_action_taken = models.CharField(max_length=100)
    type_env = models.BooleanField(default=False)
    type_inju = models.BooleanField(default=False)
    type_property = models.BooleanField(default=False)
    type_vehicle = models.BooleanField(default=False)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Incident by {self.reported_by}"
