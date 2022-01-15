from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "website/index.html")


def about(request):
    return render(request, "website/about.html")


def evolucao(request):
    return render(request, "website/evolucao.html")


def tecnologia(request):
    return render(request, "website/tecnologia.html")


def bussiness_models(request):
    return render(request, "website/bussiness_Models.html")


def interfaces(request):
    return render(request, "website/interfaces.html")


def impactos_sociais(request):
    return render(request, "website/impactos_sociais.html")


def impactos_eticos(request):
    return render(request, "website/impactos_eticos.html")


def portugal(request):
    return render(request, "website/portugal.html")


def futuro(request):
    return render(request, "website/futuro.html")
