from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("home_site/index.html")
    return HttpResponse(template.render({}, request))

def play(request):
    template = loader.get_template("home_site/play.html")
    return HttpResponse(template.render({}, request))