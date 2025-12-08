from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
import json

# Create your views here.

@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

@require_GET
def default(request):
    return JsonResponse({"status": "It's working!!!"})

@require_POST
@csrf_exempt
def echo(request):
    try:
        body = json.loads(request.body.decode("utf-8")) if request.body else {}
    except Exception:
        body = {}
    return JsonResponse({"received": body})