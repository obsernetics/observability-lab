from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=80)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name}: {self.message[:30]}"
