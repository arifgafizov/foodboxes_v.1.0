import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def recipients(request):
    recipients = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    recipients_json = recipients.json()
    return Response(recipients_json)


@api_view(http_method_names=['GET'])
def product_sets(request):
    foodboxes = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    foodboxes_json = foodboxes.json()
    return Response(foodboxes_json)
