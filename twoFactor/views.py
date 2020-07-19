from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def protected_page(request):

    if request.GET.get("logout"):
        logout(request)

    return render(request, "protected.html")
