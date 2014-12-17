from django.db import models

class Piece(models.Model):

	catalogue_id = models.CharField(max_length=45)
	heath_id = models.CharField(max_length=45, blank=True)
	piece_name = models.CharField(max_length=45, blank=True)
	piece_description = models.CharField(max_length=2000, blank=True)
	manufactured_date = models.DateField(blank=True, null=True)
	length_inches = models.IntegerField(blank=True, null=True)
	width_inches = models.IntegerField(blank=True, null=True)
	height_inches = models.IntegerField(blank=True, null=True)
	weight_ounces = models.IntegerField(blank=True, null=True)
	length_mm = models.IntegerField(blank=True, null=True)
	width_mm = models.IntegerField(blank=True, null=True)
	height_mm = models.IntegerField(blank=True, null=True)
	weight_grams = models.IntegerField(blank=True, null=True)
	cataloguer = models.CharField(max_length=45, blank=True, default="")
	catalogue_date = models.DateField(blank=True, null=True)
	condition = models.IntegerField(blank=True, null=True)
	#many to one
	exhibition = models.ForeignKey('Exhibition')
	publication = models.ForeignKey('Publication')
	
	def __str__(self):              
		return self.piece_name

class ConditionChoice(models.Model):
	conditions = (
		('a', 'Pristine' ),
		('b', 'Used, good'),
		('c', 'Used, worn'),
		('d', 'Cracked / chipped'),
		('e', 'Broken'),
		)
	name = models.CharField(max_length=60)
	condition = models.CharField(max_length=1, choices=conditions)
	

	def __str__(self):              
		return self.name

#one to many
#one publication has many pieces, foreign key is publication_id and is in table 'Pieces'
#publication = models.ForeignKey('publication')

class Publication(models.Model):
	publication_name = models.CharField(max_length=45, blank=True, default="")
	publication_date = models.DateField(blank=True, null=True)
	publication_author = models.CharField(max_length=45, blank=True, default="")
	publication_media = models.CharField(max_length=45, blank=True, default="")
	
	def __str__(self):              
		return self.publication_name


#one to many
#one exhibition has many pieces, foreign key is exibition_id and is in pieces
#exhibition = models.ForeignKey('exhibition')
class Exhibition(models.Model):
	exhibition_name = models.CharField(max_length=45, blank=True, default="")
	exhibition_date = models.DateField(blank=True, null=True)
	exhibition_description = models.CharField(max_length=1000, blank=True, default="")
	
	def __str__(self):              
		return self.exhibition_name
