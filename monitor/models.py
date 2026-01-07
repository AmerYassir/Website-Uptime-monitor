from django.db import models
from django.contrib.auth.models import User

class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='websites')
    name = models.CharField(max_length=255)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.url})"

class HealthCheck(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name='checks')
    status_code = models.IntegerField(null=True, blank=True)
    is_up = models.BooleanField(default=False)
    response_time = models.FloatField(help_text="Response time in seconds", null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        status = "UP" if self.is_up else "DOWN"
        return f"{self.website.name} - {status} at {self.timestamp}"