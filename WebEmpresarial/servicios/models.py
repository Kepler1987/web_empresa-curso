from django.db import models

# Create your models here.
class Servicio(models.Model):
	
	title = models.CharField(verbose_name='Titulo', max_length=100)
	subtitle = models.CharField(verbose_name='Subtitulo', max_length=100)
	content = models.TextField(verbose_name='Contenido')
	image = models.ImageField(verbose_name='Imagen', upload_to="servicios")
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)


	class Meta:
		verbose_name='servicio'
		verbose_name_plural='servicios'
		ordering=['created']

	def __str__(self):
		return self.title
			