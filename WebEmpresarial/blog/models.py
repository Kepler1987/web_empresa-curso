from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User 

# Create your models here.
class Categoria(models.Model):
	
	name = models.CharField(verbose_name='Nombre', max_length=100)
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)


	class Meta:
		verbose_name='categoria'
		verbose_name_plural='categorias'
		ordering=['-created']

	def __str__(self):
		return self.name

class Post(models.Model):
	
	title = models.CharField(verbose_name='Titulo', max_length=200)
	content = models.TextField(verbose_name='Contenido')
	published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
	image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
	author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
	categories = models.ManyToManyField(Categoria, verbose_name='Categorias', related_name='get_post')
	created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Edición')


	class Meta:
		verbose_name='entrada'
		verbose_name_plural="entradas"
		ordering=['-created']

	def __str__(self):
		return self.title
		