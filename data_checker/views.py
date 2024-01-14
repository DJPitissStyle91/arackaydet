from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from hashplate.models import HashedData
import json

@csrf_exempt
def check_data(request):
    if request.method == 'POST':
        posted_data = request.POST.get('data_to_check')

        data = HashedData.objects.filter(hashed_data=posted_data)
        data_exists = data.exists()
        plate = ""

        if data_exists:
            plate = list(data.values_list('plate', flat=True))[0]

        
        return JsonResponse({'data_exists': json.dumps(data_exists), 'plate': plate})
    else:
        return JsonResponse({'error': 'Invalid request method'})
