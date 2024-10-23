from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

class Command(BaseCommand):
    help = 'Imports CSV data into the database'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')
    
    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break  # Stop searching if the model is found
            except LookupError:
                continue  # Model not in current app, search next app
        
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)  # Corrected to DictReader
                for row in reader:
                    model.objects.create(**row)  # Create model instance using unpacked dictionary
                    
            self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
        
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))