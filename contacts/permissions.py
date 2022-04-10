from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm("contacts.add_contact"):
                return True
            return False
        return False
