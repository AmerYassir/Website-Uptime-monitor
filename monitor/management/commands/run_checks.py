from django.core.management.base import BaseCommand
from monitor.models import Website
from monitor.utils import check_website_health

class Command(BaseCommand):
    help = 'Runs health checks for all registered websites'

    def handle(self, *args, **kwargs):
        websites = Website.objects.all()
        self.stdout.write(f"Starting checks for {websites.count()} sites...")
        
        for website in websites:
            check_website_health(website)
            self.stdout.write(self.style.SUCCESS(f"Checked: {website.name}"))
        
        self.stdout.write(self.style.SUCCESS("All checks completed."))