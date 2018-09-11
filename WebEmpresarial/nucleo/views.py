from django.shortcuts import render, HttpResponse

def inicio(request):
	return render(request, "nucleo/inicio.html")

def historia(request):
	return render(request, "nucleo/historia.html")

def visitanos(request):
	return render(request, "nucleo/visitanos.html")




