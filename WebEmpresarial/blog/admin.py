from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title', 'author', 'published', 'post_categories')
	ordering = ('author', 'published')
	search_fields = ('title', 'content', 'author__username', 'categories__name')
	list_filter =('author__username', 'categories__name')
	date_hierarchy = 'published'

	def post_categories(self, obj):
		return ", ".join([c.name for c in obj.categories.all().order_by("name")])
	post_categories.short_description = "Categorias"

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

# Register your models here.
