from django.shortcuts import render
from django.http import HttpResponse
from app_rasyid.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render (request, 'app_rasyid/index.html', context=date_dict)