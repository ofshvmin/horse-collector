from django.db import models
from django.urls import reverse


SERVICES = ( 
  ('T', 'A Hoof Trim'),
  ('S', 'Shoes'),
  ('B', 'A Hoof Trim and Shoes')
)

# Create your models here.
class Horse(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("horse-detail", kwargs={"horse_id": self.id})

class FarrierAppt(models.Model):
  date =  models.DateField('Appointment Date')
  service = models.CharField(
    max_length=1,
    choices=SERVICES,
    default=SERVICES[0][0]
  )
  horse = models.ForeignKey(Horse, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_service_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']