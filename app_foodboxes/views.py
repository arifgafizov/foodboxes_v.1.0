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
    response_foodboxes = []

    for foodbox in foodboxes_json:
        response_foodbox = {}
        response_foodbox['title'] = foodbox['name']
        response_foodbox['description'] = foodbox['about']
        response_foodbox['price'] = foodbox['price']
        response_foodbox['weight'] = foodbox['weight_grams']
        response_foodboxes.append(response_foodbox)

    if response_foodboxes:
        result = []
        if request.query_params:
            min_price = request.query_params.get('min_price')
            min_weight = request.query_params.get('min_weight')

            if (not min_price) and (not min_weight):
                return Response(status=status.HTTP_400_BAD_REQUEST)

            for response in response_foodboxes:
                if min_price:
                    if response['price'] >= int(min_price):
                        result.append(response)
                if min_weight:
                    if response['weight'] >= int(min_weight):
                        result.append(response)

        else:
            result = response_foodboxes
        return Response(result)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def product_set(request, pk):
    foodboxes = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    foodboxes_json = foodboxes.json()
    response = {}
    for foodbox in foodboxes_json:
        if foodbox['inner_id'] == pk:
            response['title'] = foodbox['name']
            response['description'] = foodbox['about']
            response['price'] = foodbox['price']
            response['weight'] = foodbox['weight_grams']

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
