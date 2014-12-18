from django.db import models

#many to many
class Documentation(models.Model):
	documentation_name = models.CtarField(max_length=45, blank=True)
	documentation_pieces = models.ManyToManyField(Piece, through="documentation_link_piece", through_fields=('Documentation', 'Piece'))
	
	def __str__(self):              
		return self.documentation_name


class documentation_link_piece(models.Model):
	documentation = models.ForeignKey(Documentation)
	piece = models.ForeignKey(Piece)
	documentation_date = models.DateField(blank=True, null=True)
	documentation_author = models.CharField(max_length=45, blank=True)
	documentation_media = models.CharField(max_length=45, blank=True)
	documentation_location = models.CharField(max_length=45, blank=True)
	
	

#many to many
class Set_Collection(models.Model):
	set_collection_name = models.CharField(max_length=45, blank=True)
	set_collection_piece = models.ManyToManyField(Piece, through="SetCollection_link_piece", through_fields=('SetCollection', 'Piece'))
	set_collection_location = models.CharField(max_length=45, blank=True)
	
	def __str__(self):              
		return self.set_collection_name


class SetCollection_link_piece(models.Model):
	Piece = models.ForeignKey(Piece)
	SetCollection = models.ForeignKey(SetCollection)
	date = models.DateField(blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True)
	
