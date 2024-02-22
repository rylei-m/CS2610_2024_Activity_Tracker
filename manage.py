"""Django's command-line utility for administrative tasks."""
import os # This was pre-set into the program when I initialized it. I didn't use it anywhere but wasn't sure if I was supposed to delete it from here.
import sys # Same as above. Assuming Django needs it to function. 


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'activitytrackerrestart.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
