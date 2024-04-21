from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from.models import *



def fruitview(request):
    payload=[]

    db= None

    if cache.get('fruits'):    #check cache fruit are present
        payload=cache.get('fruits') # data assign in payload
        db='it is cache data...'
    else:
        db='it is database data'

        obj=Fruits.objects.all() # otherwse fetch data from db
        for i in obj:
            payload.append(i.fname)
            
        #cache.set('fruits',payload)  #payload data set in cache
        cache.set('fruits',payload,10)  #10 is a only 10 sec data store in cache after that data fetch from database we can increase or decrese time
    return JsonResponse({'status':200,'data':payload,'db':db})
