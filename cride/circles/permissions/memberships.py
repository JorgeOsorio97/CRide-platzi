"""Memberships permissions."""

# Django REST framework
from rest_framework.permissions import BasePermission

# Models
from cride.circles.models import Membership

class IsActiveCircleMember(BasePermission):
    """Allow access only to circle memberbs

    Expects that the views implementing this permission
    have a circle attribute assigned.
    """

    def has_permission(self, request, view):
        """Verify is an active circle member."""
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True

class IsSelfMember(BasePermission):
    """Allow access only to member owners."""

    def has_permission(self, request, view):
        """Let object permission grant access"""
        obj = view.get_object()
        return self.has_permission(request, view, obj)
    
    def has_object_permission(self, request, view, obj):
        """Allow access only if member is owned by requestting user."""
        return request.user == obj.user