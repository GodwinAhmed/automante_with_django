from django.core.management.base import BaseCommand

# Proposed command: python manage.py greeting {Name}

class Command(BaseCommand):
    help = "Greets the user"
    
    def add_arguments(self, parser):
        parser.add_argument('Name', type=str, help='The username to greet')
    
    def handle(self, *args, **kwargs):
        # Write the logic here 
        name = kwargs['name']
        greeting =f'Hi{name}, Good Morning'
        self.stdout.write(self.style.SUCCESS(greeting))