# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    request.session.setdefault("times", 0)
    request.session["times"] += 1
    context = {
        "number":request.session["times"],
        "word":get_random_string(14)
    }
    return render(request, "wordApp/index.html", context)
def reset(request):
    request.session["times"] = 0
    return redirect("/")