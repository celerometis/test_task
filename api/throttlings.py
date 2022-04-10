from rest_framework.throttling import UserRateThrottle


class ThrottlingChangePhoneUser(UserRateThrottle):
    scope = 'phone'

    def get_ident(self, request):
        return request.data['phone']
