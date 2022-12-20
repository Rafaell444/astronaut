from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard/pages/home.html")


def WebsiteSettings(request):
    return render(request, "dashboard/pages/websettings.html")
