#heart
from django.contrib import admin
from django.db import models
from .models import Piece, ConditionChoice, Publication, Exhibition

# Register your models here.
class PieceAdmin(admin.ModelAdmin):
	pass
    
admin.site.register(Piece, PieceAdmin)

class ConditionChoiceAdmin(admin.ModelAdmin):
	pass	

	admin.site.register(ConditionChoice, ConditionChoiceAdmin)

#one to many
#one publication has many pieces, foreign key is publication_id and is in table 'Pieces'
#publication = models.ForeignKey('publication')

class PublicationAdmin(admin.ModelAdmin):
	pass	
	
	admin.site.register(Publication, PublicationAdmin)


#one to many
#one exhibition has many pieces, foreign key is exibition_id and is in pieces
#exhibition = models.ForeignKey('exhibition')
class ExhibitionAdmin(admin.ModelAdmin):
	pass	
	
	admin.site.register(Exhibition, ExhibitionAdmin)

