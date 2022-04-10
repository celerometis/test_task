from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # we can use it
    # def perform_create(self, serializer):
    #     print(serializer)
    #     serializer.save()


class ContactDetailAPIView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # lookup_field = 'pk'  we can use it to other field lookup


# class ContactListAPIView(generics.ListAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer
#     # lookup_field = 'pk'  we can use it to other field lookup


class ContactUpdateAPIView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDestroyAPIView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

@api_view(['GET', 'POST'])
def contact_crl_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Contact, pk=pk)
            data = ContactSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Contact.objects.all()
        data = ContactSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
