from pprint import pprint

from django.shortcuts import render

from flower_app.models import Bouquet, Consultation, Place, Category, Composition


def index(request):
	bouquets = Bouquet.objects.all()[:3]
	places = Place.objects.all()
	return render(request, 'index.html', context={'bouquets': bouquets, 'places': places})


def card(request):
	return render(request, 'card.html')


def catalog(request):
	bouquets = Bouquet.objects.all()
	return render(request, 'catalog.html', context={'bouquets': bouquets})


def consultation(request):
	if request.method == 'POST':
		name = request.POST['fname']
		phone_number = request.POST['tel']
		new_consultation = Consultation.objects.create(name=name, phone_number=phone_number)
		new_consultation.save()
	return render(request, 'consultation.html')


def order(request):
	return render(request, 'order.html')


def order_step(request):
	return render(request, 'order-step.html')


def quiz(request):
	context = {
		'categories': Category.objects.all()
	}
	return render(request, 'quiz.html', context=context)


def quiz_step(request):

	print(request.GET.get('category'))
	return render(request, 'quiz-step.html')


def result(request):
	return render(request, 'result.html')

