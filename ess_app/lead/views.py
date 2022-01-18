from django.shortcuts import render

from rest_framework import viewsets

from .models import Lead
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all() 

    '''Below query restricts leads for User who owns them'''

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)

    '''Below query passes UserID who created Lead'''

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    
