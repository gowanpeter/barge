from django.db import models

class Piece(models.Model):
	catalogue_id = models.CharField(max_length=45)
	heath_id = models.CharField(max_length=45, blank=True)
	piece_name = models.CharField(max_length=45, blank=True)
	piece_description = models.CharField(max_length=2000,  	blank=True)
	manufactured_date = models.DateField(blank=True, null=True)
