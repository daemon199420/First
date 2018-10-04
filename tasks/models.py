from django.db import models
from accounts.models import MyUser

class Task (models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    executor = models.ForeignKey(MyUser, related_name="executor", on_delete=models.DO_NOTHING, null=True)
    manager = models.ForeignKey(MyUser, related_name="manager", on_delete=models.DO_NOTHING, null=True)
