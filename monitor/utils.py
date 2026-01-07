import requests
from django.utils import timezone
from .models import HealthCheck

def check_website_health(website):
    try:
        start_time = timezone.now()
        response = requests.get(website.url, timeout=10)
        end_time = timezone.now()
        
        duration = (end_time - start_time).total_seconds()
        
        HealthCheck.objects.create(
            website=website,
            status_code=response.status_code,
            is_up=200 <= response.status_code < 400,
            response_time=duration
        )
        print(f"Checked {website.url}: {response.status_code} in {duration} seconds")
    except requests.RequestException:
        HealthCheck.objects.create(
            website=website,
            is_up=False,
            status_code=None
        )

        