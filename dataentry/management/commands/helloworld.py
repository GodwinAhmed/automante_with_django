from django.core.management.base import BaseCommand
#from django.core.management import call_command
#from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Print Hello Django"
    
    def handle(self, *args, **kwargs):
        #Write the logig  here
        self.stdout.write('Hello  Django\n')

