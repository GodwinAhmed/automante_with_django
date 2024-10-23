import csv
from django.core.management.base import BaseCommand
from django.apps import apps
from dataentry.utils import generate_csv_file

class Command(BaseCommand):
    help = 'Export data from the database to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        # Search through all the installed apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break  # Stop executing once the model is found
            except LookupError:
                continue  # Continue searching in other apps
        
        if not model:
            self.stderr.write(self.style.ERROR(f'Model "{model_name}" could not be found.'))
            return
        
        # Fetch the data from the database
        data = model.objects.all()

        # Generate CSV file path
        file_path = generate_csv_file(model_name)

        # Open the CSV file and write the data
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write the CSV header
            writer.writerow([field.name for field in model._meta.fields])

            # Write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {file_path}!'))