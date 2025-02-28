import os
import sys
import socket

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    if "runserver" in sys.argv and not any(arg.startswith("0.0.0.0") for arg in sys.argv):
        # This sets the port only if it's not already provided
        port = os.getenv("PORT", "5000")  # Default to 5000 if no environment variable is set
        sys.argv.append(f"0.0.0.0:{port}")


    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
