import datetime
import jwt
import re

from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializer import UserSerializer


class UserRegisterView(APIView):
    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                user.is_active = True
                user.save()

                return Response({'messages': 'Reguisteration Success'})

        except Exception as e:
            error_messages = str(e)
            required_messages = {}
            # Error message filtering
            for match in re.finditer(r"'(.*?)': \[ErrorDetail\(string='(.*?)', code='(.*?)'\)\]", error_messages):
                field, message = match.group(1), match.group(2)
                if field != 'unknown':  
                    required_messages[field] = message

            return Response({'messages': required_messages}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

class LoginUserView(APIView):
    def post(self, request):
        # Check if 'email' and 'password' keys are present in request.data
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'message': 'Both email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        tokens = user.token() 

        response = Response()
        response.set_cookie(key='jwt', value=tokens['access'], httponly=True)
        response.data = {
            'message': 'Success',
            'access_token': tokens['access'],
            'refresh_token': tokens['refresh']
        }
        return response
  

class ViewProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # If the user is authenticated, request.user contains the authenticated user instance
        user = request.user
        serializer = UserSerializer(user)
        
        response_data = {
            'username': serializer.data['first_name'],
        }
        
        return Response(response_data)
      
class LogoutView(APIView):
    def post(self,request):
        response =Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'Logout Success'
        }
        
        return response
    


