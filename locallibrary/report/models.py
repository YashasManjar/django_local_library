from django.db import models

# Create your models here.
#Document Report
from django.urls import reverse # Used in get_absolute_url() to get URL for specified ID

from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

class DocuementReport(models.Model):
    """Model representing a doc (but not a specific report of a doc)."""
    clientid = models.CharField(max_length=20)
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter the client name"
        
    )
    #name = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    docid = models.CharField(max_length=20)
    #docid = models.ManyToManyField(
       # Docid, help_text="Select a doc for this report")
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('doc-detail', args=[str(self.id)])

#Reference Report
class ReferenceReport(models.Model):
    """Model representing a doc (but not a specific report of a ref)."""
    clientid = models.CharField(max_length=20)
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter the client name"
        
    )
    caseid = models.CharField(max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('ref-detail', args=[str(self.id)])
