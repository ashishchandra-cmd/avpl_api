from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle

class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'viewstu'

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  throttle_classes = [ScopedRateThrottle]
  throttle_scope = 'modifystu'


from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
]

===================================================================
from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song

class SingerViewSet(viewsets.ModelViewSet):
 queryset = Singer.objects.all()
 serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
 queryset = Song.objects.all()
 serializer_class = SongSerializer

from django.db import models

# Create your models here.
class Singer(models.Model):
 name = models.CharField(max_length=100)
 gender = models.CharField(max_length=100)

 def __str__(self):
  return self.name

class Song(models.Model):
 title = models.CharField(max_length=100)
 singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song') 
 duration = models.IntegerField()

 def __str__(self):
  return self.title

from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
 class Meta:
  model = Song
  fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
 # song = serializers.StringRelatedField(many=True, read_only=True)
 # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
 # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
 # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='duration')
 song = serializers.HyperlinkedIdentityField(view_name='song-detail')
 class Meta:
  model = Singer
  fields = ['id', 'name', 'gender', 'song']


from django.shortcuts import render
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets
from .models import Singer, Song

class SingerViewSet(viewsets.ModelViewSet):
 queryset = Singer.objects.all()
 serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
 queryset = Song.objects.all()
 serializer_class = SongSerializer


from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
=============================================================

class SongSerializer(serializers.ModelSerializer):
 class Meta:
  model = Song
  fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
 sungby = SongSerializer(many=True, read_only=True)
 class Meta:
  model = Singer
  fields = ['id', 'name', 'gender', 'sungby']


class SingerViewSet(viewsets.ModelViewSet):
 queryset = Singer.objects.all()
 serializer_class = SingerSerializer

class SongViewSet(viewsets.ModelViewSet):
 queryset = Song.objects.all()
 serializer_class = SongSerializer
======================================================
from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
 def list(self, request):
  print("*********List***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

 def retrieve(self, request, pk=None):
  print("*********Retrieve***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  id = pk
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

 def create(self, request):
  print("*********Create***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def update(self,request, pk):
  print("*********Update***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def partial_update(self,request, pk):
  print("*********Partial Update***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def destroy(self,request, pk):
  print("*********Destroy***********")
  print("Basename:", self.basename)
  print("Action:", self.action)
  print("Detail:", self.detail)
  print("Suffix:", self.suffix)
  print("Name:", self.name)
  print("Description:", self.description)
  id = pk
  stu = Student.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})



from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]

=======================
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


class StudentList(ListAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer



from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),

    path('studentapi/', views.StudentListCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrieveDestroy.as_view()),
    path('studentapi/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),
]

===================================


# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# List and Create - PK Not Required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)

 def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)

# Retrieve Update and Destroy - PK Required
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)

 def put(self, request, *args, **kwargs):
  return self.update(request, *args, **kwargs)

 def delete(self, request, *args, **kwargs):
  return self.destroy(request, *args, **kwargs)



from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/', views.RUDStudentAPI.as_view()),
]


=================
# GenericAPIView and Model Mixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class StudentList(GenericAPIView, ListModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.list(request, *args, **kwargs)

class StudentCreate(GenericAPIView, CreateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def post(self, request, *args, **kwargs):
  return self.create(request, *args, **kwargs)

class StudentRetrive(GenericAPIView, RetrieveModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def get(self, request, *args, **kwargs):
  return self.retrieve(request, *args, **kwargs)

class StudentUpdate(GenericAPIView, UpdateModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def put(self, request, *args, **kwargs):
  return self.update(request, *args, **kwargs)

class StudentDestroy(GenericAPIView, DestroyModelMixin):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer

 def delete(self, request, *args, **kwargs):
  return self.destroy(request, *args, **kwargs)



from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
    # path('studentapi/', views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/', views.StudentRetrive.as_view()),
    # path('studentapi/<int:pk>/', views.StudentUpdate.as_view()),
    path('studentapi/<int:pk>/', views.StudentDestroy.as_view()),
]

==============

from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class StudentAPI(APIView):
 def get(self, request, pk=None, format=None):
  id = pk
  if id is not None:
   stu = Student.objects.get(id=id)
   serializer = StudentSerializer(stu)
   return Response(serializer.data)

  stu = Student.objects.all()
  serializer = StudentSerializer(stu, many=True)
  return Response(serializer.data)

 def post(self, request, format=None):
  serializer = StudentSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def put(self, request, pk, format=None):
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 def patch(self, request, pk, format=None):
  id = pk
  stu = Student.objects.get(pk=id)
  serializer = StudentSerializer(stu, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 def delete(self, request, pk, format=None):
  id = pk
  stu = Student.objects.get(pk=id)
  stu.delete()
  return Response({'msg':'Data Deleted'})




from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/', views.StudentAPI.as_view()),
]
