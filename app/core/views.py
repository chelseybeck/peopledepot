from django.shortcuts import render

# Create your views here.
from .models import Project
from .models import RecurringEvent
from .models import User


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_r_events = RecurringEvent.objects.all().count()
    num_projects = Project.objects.all().count()

    # The 'all()' is implied by default.
    num_users = User.objects.count()

    context = {
        "num_r_events": num_r_events,
        "num_projects": num_projects,
        "num_users": num_users,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
