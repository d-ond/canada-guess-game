import random
from django.shortcuts import render
from django.http import JsonResponse
from .models import City

def index(request):
    all_cities = list(City.objects.all())
    target_city = random.choice(all_cities)
    request.session['target_city_id'] = target_city.id
    return render(request, 'cities/index.html', {'cities': all_cities})

def check_guess(request):
    target_city_id = request.session.get('target_city_id')
    target_city = City.objects.get(id=target_city_id)

    user_guess_id = int(request.GET.get('guess_id'))
    user_guess = City.objects.get(id=user_guess_id)

    feedback = {
        'is_correct': False,
        'city_name': user_guess.city_name,
        'city_province': user_guess.city_province,
        'city_population': user_guess.city_population,
        'city_area': user_guess.city_area,
        'population_feedback': '',
        'province_feedback': '',
        'area_feedback': ''
    }

    if user_guess.id == target_city.id:
        feedback['is_correct'] = True
    else:
        feedback['population_feedback'] = 'same' if user_guess.city_population == target_city.city_population else ('higher' if user_guess.city_population < target_city.city_population else 'lower')
        feedback['province_feedback'] = 'same' if user_guess.city_province == target_city.city_province else 'different'
        feedback['area_feedback'] = 'same' if user_guess.city_area == target_city.city_area else ('larger' if user_guess.city_area < target_city.city_area else 'smaller')

    return JsonResponse(feedback)
