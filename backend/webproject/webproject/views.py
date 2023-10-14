from django.http import JsonResponse
import datetime

def api_health_check(request):

    response_object = {
        "status" : "ok",
        "time" : datetime.datetime.now()
    }

    return JsonResponse(response_object, status=200)