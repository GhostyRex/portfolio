from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    # User that inputs the project in the db.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # The image of the project
    image = models.ImageField(upload_to='projects')

    # The redirect link that we go to when the project image is clicked.
    link = models.CharField(max_length=200, null=True, blank=True)

    # Tells if a project is hosted or not.
    hosted = models.BooleanField(default=False)

    # Created on
    created_on = models.DateTimeField()
