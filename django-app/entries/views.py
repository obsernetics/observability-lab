from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Entry

def index(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        message = (request.POST.get("message") or "").strip()
        if name and message:
            Entry.objects.create(name=name[:80], message=message[:500])
        return redirect("index")
    entries = Entry.objects.all()[:50]
    return render(request, "entries/index.html", {"entries": entries})

def healthz(request):
    return HttpResponse("ok", content_type="text/plain")
