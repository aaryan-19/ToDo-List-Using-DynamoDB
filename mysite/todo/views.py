from django.shortcuts import render
from .models import DynamoDB
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from datetime import date

obj = DynamoDB()

# Create your views here.
from django.http import HttpResponse, HttpRequest

def index(request):
    """Index Page"""
    return HttpResponse("Hello, world. You're at the todo index.")

@csrf_exempt
def insert(request):
    """Insertion"""
    data = json.loads(request.body.decode('utf-8'))
    append_data = {
        "status": "incomplete",
        "entry_date": str(date.today())
    }
    data.update(append_data)
    print(data)
    response = obj.insert(data)
    print(response)
    json_data = {"status": "Insertion Completed"}
    return_data = json.dumps(json_data)
    return HttpResponse(return_data, content_type='application/json')
    # return HttpResponse("Successfull Entry")

@csrf_exempt
def update(request):
    """Update"""
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    response = obj.update(data['entry_date'], data['task_id'])
    print(response)
    json_data = {"status": "Updation Successful"}
    return_data = json.dumps(json_data)
    return HttpResponse(return_data, content_type='application/json')

def view(request):
    """View All Items"""
    response = obj.read_all()
    print(response)
    return HttpResponse(response['Items'])

@csrf_exempt
def view_single_item(request):
    """"View Single item"""
    data = json.loads(request.body.decode('utf-8'))
    
    response = obj.read_single_item(data['entry_date'], str(data['task_id']))
    
    json_data = json.dumps(response)

    return HttpResponse(json_data, content_type='application/json')
   

@csrf_exempt
def delete_item(request):
    """Deletion"""
    data = json.loads(request.body.decode('utf-8'))
    # print(data)
    response = obj.delete_single_item(data['entry_date'], data['task_id'])
    print(response)
    json_data = {"status": "Deletion Successful"}
    return_data = json.dumps(json_data)
    return HttpResponse(return_data, content_type='application/json')
    # return HttpResponse("Deletion Completed")