from django.shortcuts import render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.models import CheckList
from backend.serializers import CheckListSerializer
from backend.serializers import CheckListShowSerializer


@csrf_exempt
def checklistsapi_show(request):
    if request.method == 'GET':
        checklists = CheckList.objects.all()
        serializer = CheckListShowSerializer(checklists, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def checklistapi_detail(request, pk):
    try:
        checklist = CheckList.objects.get(pk=pk)
    except CheckList.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CheckListSerializer(checklist)
        return JsonResponse(serializer.data, safe=False)



