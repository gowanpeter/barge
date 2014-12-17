#places
from django.contrib import admin

class DocumentationAdmin(admin.ModelAdmin):

	admin.site.register(Documentation, DocumentationAdmin)
	
class documentation_link_pieceAdmin(admin.ModelAdmin):

	admin.site.register(documentation_link_piece, documentation_link_pieceAdmin)
	
#many to many
class Set_CollectionAdmin(admin.ModelAdmin):

	admin.site.register(Set_Collection, Set_CollectionAdmin)

class SetCollection_link_pieceAdmin(admin.ModelAdmin):

	admin.site.register(SetCollection_link_piece, SetCollection_link_pieceAdmin)
