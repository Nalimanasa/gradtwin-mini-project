from django.http import JsonResponse
from .models import Item   #

# Create your views here.
def Register(request):
    items=Item.objects.all().values()
    return JsonResponse(list(items), safe=False)