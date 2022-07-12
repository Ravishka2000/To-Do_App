from django.db import models


class Todo(models.Model):
    task_title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_title}'
