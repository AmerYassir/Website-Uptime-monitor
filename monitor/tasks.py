from celery import shared_task
from .models import Website
from .utils import check_website_health

@shared_task
def check_all_websites_task():
    """
    Background task that iterates through all websites 
    and triggers a health check for each.
    """
    websites = Website.objects.all()
    
    for website in websites:
        # We call the utility function we tested earlier
        check_website_health(website)
        
    return f"Checked {websites.count()} websites."