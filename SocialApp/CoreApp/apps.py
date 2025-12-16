from django.apps import AppConfig


class CoreappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CoreApp'

    def ready(self):
        # Import the function and call it during app initialization
        # Wrapped in try-except to handle DB unavailability during Docker boot
        try:
            from .admin import create_support_group
            create_support_group()
        except Exception as e:
            # Database might not be ready yet (Docker networking, migrations pending, etc.)
            print(f"Skipping group creation during boot: {e}")
