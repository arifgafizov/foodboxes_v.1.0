import requests
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=['GET'])
def recipients(request):
    recipients = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    recipients_json = recipients.json()
    response = []

    for recipient in recipients_json:
        response_recipient = recipient['info']
        response_recipient['phoneNumber'] = recipient['contacts']['phoneNumber']
        response.append(response_recipient)

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def recipient(request, pk):
    recipients = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    recipients_json = recipients.json()
    response = None
    for recipient in recipients_json:
        if recipient['id'] == pk:
            response = recipient['info']
            response['phoneNumber'] = recipient['contacts']['phoneNumber']

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def product_sets(request):
    foodboxes = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    foodboxes_json = foodboxes.json()
    return Response(foodboxes_json)
