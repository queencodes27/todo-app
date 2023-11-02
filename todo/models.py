from django.db import models


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_att = models.DateTimeField(auto_now_add=True)
    update_att = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'

# Create your models here.
