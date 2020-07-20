from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def trx_bot(request):
    if request.method == 'POST':
        viber.jason.loads(request.body.decode('utf-8'))
        if viber['event'] == 'webhook':
            print(viber)
            print('Webhook successfully established')
            retrunHttpResponse(status=200)
        else:
            print('This is not a Webhook - try again or use POSTMAN')
            return HttpResponse(status=500)
    return HttpResponse(status=200)
