from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from website.api.serializers import MessageSerializer
from website.models import Message


@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data)


@api_view(['GET'])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)

    return Response(serialized_message.data)


@api_view(['POST'])
def create_message(request):
    if request.method == 'POST':
        serialized_message = MessageSerializer(data=request.data)
        if serialized_message.is_valid():
            serialized_message.author = request.user
            serialized_message.save()
            return Response(serialized_message.data, status=status.HTTP_201_CREATED)
        return Response(serialized_message.errors, status=status.HTTP_400_BAD_REQUEST)
