from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=200, blank=True, default='')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return "TODO: [Task = {}; Complete = {}]".format(self.task, self.complete)
