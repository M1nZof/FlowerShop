from django.shortcuts import render

from flower_app.models import Bouquet, Consultation, Place, Category


def index(request):
	bouquets = Bouquet.objects.all()[:3]
	places = Place.objects.all()
	return render(request, 'index.html', context={'bouquets': bouquets, 'places': places})


def card(request, bouquet_id):
	bouquet = Bouquet.objects.get(id=bouquet_id)

	context = {
		'bouquet': bouquet,
	}
	return render(request, 'card.html', context=context)


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
	category = request.GET.get('category')
	request.session['category'] = category
	prices = set(
		f'{(bouquet.price // 1000) * 1000} - {(bouquet.price // 1000 + 1) * 1000} руб.'
		for bouquet in Category.objects.get(title=category).bouquets.all()
	)
	prices.add('Не имеет значения')
	context = {
		'prices': sorted(prices)
	}
	return render(request, 'quiz-step.html', context=context)


def result(request):
	prices = request.GET.get('price')
	category = request.session['category']
	bouquets = Category.objects.get(title=category).bouquets.all()
	if prices != 'Не имеет значения':
		min_price, max_price = [int(s) for s in prices.split() if s.isdigit()]
		bouquets = [
			bouquet for bouquet
			in bouquets
			if min_price < bouquet.price < max_price
		]

	context = {
		'bouquets': [
			{
				'id': bouquet.id,
				'title': bouquet.name,
				'description': bouquet.description,
				'compositions': ', '.join(map(str, bouquet.composition.all())),
				'image': bouquet.image.url,
				'price': bouquet.price,
			}
			for bouquet in bouquets
		]
	}
	return render(request, 'result.html', context=context)

