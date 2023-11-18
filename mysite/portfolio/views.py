from django.shortcuts import render, redirect
from .models import Project

# Math function imports.
from math import ceil

# Pagination imports.
from django.core.paginator import Paginator


# Create your views here.
# Handle 404 pages.
def error_404_view(request, exception):
    # data = {"name": "ThePythonDjango.com"}
    # return render(request,'myapp/error_404.html', data)
    # print('404 done')
    return redirect('index')


def index(request):
    # Get all the projects. Now filter them based on hosted and not hosted.
    gotProjects = Project.objects.all().order_by('-id')

    # WE need 3 sets of 4.
    # Set one, the all set.
    # This set will be made of the first 4 last entry projects in reverse i.e, the latest projects.
    allSet = {}

    try:
        allSet['0'] = gotProjects[0]
        allSet['1'] = gotProjects[1]
        allSet['2'] = gotProjects[2]
        allSet['3'] = gotProjects[3]

    except IndexError:
        pass

    # Set 2, the hosted set.
    allHosted = gotProjects.filter(hosted=True)

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
    allNotHosted = gotProjects.filter(hosted=False)

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
        'all': [allSet, len(gotProjects)],
        'hosted': [chosenHosted, len(allHosted)],
        'not_hosted': [chosenNotHosted, len(allNotHosted)]
    }

    return render(request, template_name='portfolio/general/index.html', context=context)


def projects(request):
    # 1. Read the gallery folder to get the name of all the files in the gallery.
    images = Project.objects.filter().order_by('hosted')

    # Set gallery to True.
    # active_gallery = True

    # 2. We need to split the images into grids of 3. i.e. each row having 3 columns.
    img_length = len(images)

    # Round up if there are extra gallery that don't make up the 3 column sequence
    num_rows = ceil(img_length / 3)

    temp_list = []

    image_list = []

    reversed_image = list(reversed(images))

    # Get the images in list of 3.
    for i in range(img_length):
        temp_list.append(reversed_image[i])

        if (i + 1) % 3 == 0 and i + 1 > 2:
            image_list.append(temp_list)

            temp_list = []

    # If there is still some last images that did not round up to 3, then we add them.
    if temp_list:
        image_list.append(temp_list)

    print(image_list)

    # Create paginator for the gotten members.
    # Here, we use 3 since the videos come in sets of 3's.
    paginator = Paginator(image_list, 3)  # Show 50 contacts per page.

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    # End paginator.

    # 2. Pass the name as context to the gallery.html which will use django to render the gallery pictures.
    # We need the latest pictures first so, we reverse the filter.
    context = {
        'page_obj': page_obj,
        'rows': range(num_rows),
    }

    return render(request, template_name='portfolio/general/projects.html', context=context)
