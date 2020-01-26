from django.shortcuts import render
import requests
import json


def about(request):
    return render(request,'about.html')


def index(request):
    api_request=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE:RELIANCE&apikey=BP39EYKNTFWF2FOF")
    try:
        api=json.loads(api_request.content)
    except Exception as e:
        api="Error"
    return render(request,'index.html',{'api':api})
