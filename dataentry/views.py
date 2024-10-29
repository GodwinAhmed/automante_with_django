from django.shortcuts import render, redirect
from .utils import get_all_custom_models

# Create your views here.
def import_data_view(request):
    if request.method == 'POST':
        # Handle the POST request data here
        # For example, process the form data and save it
        # After processing, redirect to a success page or render a message
        # return redirect('success_url')  # Example of redirecting after processing
        pass  # Replace with your logic

    # If the request is GET or if POST processing is not done
    all_models = get_all_custom_models()
    
    return render(request, 'dataentry/import_data.html', {'all_models': all_models})