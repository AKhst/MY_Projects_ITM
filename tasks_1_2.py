import logging

# Проверьте атрибуты объекта logging
if hasattr(logging, 'Logger') and hasattr(logging, 'DEBUG'):
    print("Logging module has been successfully imported.")
