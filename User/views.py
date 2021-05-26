from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import send_mail
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from _thread import start_new_thread
from .models import all_user
# Create your views here.

def mail_send(name,email):
	print(email)
	send_mail(
			'Your Account Is Succesfully Created.',
			'Hello ' +
			name +
			' Your Account Is Succesfully Created on Our Portal  ',
			'vivekprasad2992@gmail.com',
			[email],
			fail_silently=False,
			html_message='Hello ' +
			name + '<h3 style="color:red">Congratulations !</h3> Your Account Is Succesfully Created on Our Portal.',
		)


class UserCreateAPI(APIView):
	def get(self, request, *args, **kwargs):
		User = all_user.objects.all()
		serializer = UserSerializer(User, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		user_data = request.data
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			start_new_thread(mail_send, (user_data['name'],user_data['email']))
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
