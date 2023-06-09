#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatGPT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc 
    if sys.argv[1] == 'migrate':
        from django.conf import settings
        from django.db.migrations import AlterField
        if settings.DATABASES['default']['ENGINE'] == 'djongo':
            AlterField.database_forwards = lambda *_: None
            AlterField.database_backwards = lambda *_: None
    execute_from_command_line(sys.argv)
