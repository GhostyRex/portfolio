from django.shortcuts import render, redirect
from .models import Project


# Create your views here.
# Handle 404 pages.
def error_404_view(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    # return render(request,'myapp/error_404.html', data)
    # print('404 done')
    return redirect('index')


def index(request):
    # Get all the projects. Now filter them based on hosted and not hosted.
    projects = Project.objects.all().order_by('-id')

    # WE need 3 sets of 4.
    # Set one, the all set.
    # This set will be made of the first 4 last entry projects in reverse i.e, the latest projects.
    allSet = {}

    try:
        allSet['0'] = projects[0]
        allSet['1'] = projects[1]
        allSet['2'] = projects[2]
        allSet['3'] = projects[3]

    except IndexError:
        pass

    # Set 2, the hosted set.
    allHosted = projects.filter(hosted=True)

    # List to hold the chosen hosted.
    chosenHosted = {}

    try:
        chosenHosted['0'] = allHosted[0]
        chosenHosted['1'] = allHosted[1]
        chosenHosted['2'] = allHosted[2]
        chosenHosted['3'] = allHosted[3]

    except IndexError:
        pass

    # Filter out the not hosted.
    allNotHosted = projects.filter(hosted=False)

    # List to hold the chosen not hosted.
    chosenNotHosted = {}

    try:
        chosenNotHosted['0'] = allNotHosted[0]
        chosenNotHosted['1'] = allNotHosted[1]
        chosenNotHosted['2'] = allNotHosted[2]
        chosenNotHosted['3'] = allNotHosted[3]

    except IndexError:
        pass

    # Get the
    # Set 3, the not-hosted set.
    context = {
        'all': [allSet, len(projects)],
        'hosted': [chosenHosted, len(allHosted)],
        'not_hosted': [chosenNotHosted, len(allNotHosted)]
    }

    return render(request, template_name='portfolio/general/index.html', context=context)
