from rest_framework import generics, mixins, permissions, authentication
from api.authentication import TokenAuthentication
from .models import Contact
from .serializers import ContactSerializer
from .permissions import IsStaffPermission
from rest_framework.throttling import UserRateThrottle
from api.throttlings import ThrottlingChangePhoneUser

class ContactMixinView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsStaffPermission]
    throttle_classes = [UserRateThrottle, ThrottlingChangePhoneUser]
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
