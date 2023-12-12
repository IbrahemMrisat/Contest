# contest/models.py
from django.db import models
import requests,json
lambda_url = 'https://7gvuerif2qbg6ed4kf6gkc4wge0gtdsy.lambda-url.us-west-1.on.aws/'

class Contestant(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, unique=True)

    def __init__(self,full_name,phone_number):
        self.full_name =full_name 
        self.phone_number =phone_number
        insert_user(self.full_name,self.phone_number)
def insert_user(full_name,phone_number):
    print(full_name,phone_number)
    payload = {"fullName":full_name,
             "phoneNumber":phone_number
        }
    
    headers = {
    "Content-Type": "application/json"
}

    response = requests.post(lambda_url, json=payload, headers=headers)

    return response.status_code
