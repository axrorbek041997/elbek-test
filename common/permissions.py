from rest_framework.permissions import BasePermission


class RoleBasedPermission(BasePermission):
    message = 'Permission denied!'

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        if not hasattr(view, 'permission_codes'):
            return False

        if type(view.permission_codes) is list:
            if not len(view.permission_codes):
                return True

            return request.user.has_perms(view.permission_codes)

        if type(view.permission_codes) is dict:
            method = request.method.upper()
            return request.user.has_perm(view.permission_codes.get(method))


class CustomPermissions:
    class BOOKING:
        CREATE_BOOKING = 'create_booking'
        VIEW_BOOKING = 'view_booking'
        UPDATE_BOOKING = 'update_booking'
        DELETE_BOOKING = 'delete_booking'

        class META:
            APP = 'base'
            CREATE_BOOKING = f'{APP}.create_booking'
            VIEW_BOOKING = f'{APP}.view_booking'
            UPDATE_BOOKING = f'{APP}.update_booking'
            DELETE_BOOKING = f'{APP}.delete_booking'

    class PITCH:
        CREATE_PITCH = 'create_pitch'
        VIEW_PITCH = 'view_pitch'
        UPDATE_PITCH = 'update_pitch'
        DELETE_PITCH = 'delete_pitch'

        class META:
            APP = 'base'
            CREATE_PITCH = f'{APP}.create_pitch'
            VIEW_PITCH = f'{APP}.view_pitch'
            UPDATE_PITCH = f'{APP}.update_pitch'
            DELETE_PITCH = f'{APP}.delete_pitch'

    class ADDRESS:
        CREATE_ADDRESS = 'create_address'
        VIEW_ADDRESS = 'view_address'
        UPDATE_ADDRESS = 'update_address'
        DELETE_ADDRESS = 'delete_address'

        class META:
            APP = 'base'
            CREATE_ADDRESS = f'{APP}.create_address'
            VIEW_ADDRESS = f'{APP}.view_address'
            UPDATE_ADDRESS = f'{APP}.update_address'
            DELETE_ADDRESS = f'{APP}.delete_address'

    class MEDIA:
        CREATE_MEDIA = 'create_media'
        VIEW_MEDIA = 'view_media'
        UPDATE_MEDIA = 'update_media'
        DELETE_MEDIA = 'delete_media'

        class META:
            APP = 'base'
            CREATE_MEDIA = f'{APP}.create_media'
            VIEW_MEDIA = f'{APP}.view_media'
            UPDATE_MEDIA = f'{APP}.update_media'
            DELETE_MEDIA = f'{APP}.delete_media'
