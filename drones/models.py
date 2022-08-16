from django.db import models
from django.utils.text import slugify

# Create your models here.
class DroneCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(DroneCategory, self).save(*args, **kwargs)

class Drone(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    drone_category = models.ForeignKey(DroneCategory, on_delete=models.CASCADE, related_name='drones')
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Drone, self).save(*args, **kwargs)

class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    name = models.CharField(max_length=255, unique=True, blank=False)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE)
    races_count = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Competition(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='competitions')
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        # Order by distance in descending order
        ordering = ('-distance_in_feet',)