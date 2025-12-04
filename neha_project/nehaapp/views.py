from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def neha_list(request):
    students = [
        {'name': 'minni', 'marks': 85},
        {'name': 'sai', 'marks': 90},
        {'name': 'mani', 'marks': 100},
        {'name': 'lohith', 'marks': 50},
    ]
    passmarks = 50  # Define passing marks threshold
    return render(request, 'nehaapp/neha_list.html', {'students': students, 'passing_marks': passmarks})
