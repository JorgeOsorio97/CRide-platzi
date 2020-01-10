""" Django.models.utilities"""

# Django
from django.db import models

class CRideModel(models.Model):
    """ Comparte Ride base model.
    CRideModel acts as an abstract base class from which every
    other model in the project will inherit.
    This class provides every table with the followint attributes:
        * Created (DateTime): The datetime when model was created.
        * modified (DateTime): FalseThe last datetime the object was modified.
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='DateTime on which the object was created'
    )
    modified = models.DateTimeField('modified at',
        auto_now=True,
        help_text='Datetime on which the object was las modified'
    )

    class Meta:
        """ Meta options """
        abstract = True
        
        get_latest_by = "created"
        ordering = ['-created', '-modified']