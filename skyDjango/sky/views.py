from django.shortcuts import render
from .models import SkyColor , Season
from django.shortcuts import get_object_or_404
from .forms import SkyColorForm 


# Create your views here.
def all_sky(request):
    skies = (
        SkyColor.objects.all()
    )  # this gives array keep in mind what value u will get
    return render(request, "sky/all_sky.html", {"skies": skies})


def sky_detail(request, sky_id):
    sky = get_object_or_404(SkyColor, pk=sky_id)
    return render(request, "sky/sky_detail.html", {"sky": sky})


def sky_season(request):

    return render(request, "sky/sky_season.html")
