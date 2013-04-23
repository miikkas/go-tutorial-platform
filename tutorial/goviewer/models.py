from datetime import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class MyModel(models.Model):
    """
    Description.
    """

    def __str__(self):
        return ""

