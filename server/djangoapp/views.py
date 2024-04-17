from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import CarMake, CarModel
from .restapis import get_request, post_review
from .populate import initiate  # Ensure this is defined in your populate.py

logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        response_data = {
            'userName': username, 
            'status': 'Authenticated'
        }
        return JsonResponse(response_data)
    return JsonResponse({
        'userName': username, 
        'status': 'Authentication failed'
    })

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({'status': 'Logged out'})
    return JsonResponse({
        'error': 'User not authenticated'
    }, status=400)

@csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username, password = data['userName'], data['password']
    first_name, last_name, email = data['firstName'], data['lastName'], data['email']
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'Username exists'}, status=400)
    user = User.objects.create_user(
        username, email, password,
        first_name=first_name, last_name=last_name
    )
    login(request, user)
    return JsonResponse({
        'userName': username, 
        'status': 'Registered and logged in'
    })

def get_dealerships(request, state="All"):
    endpoint = "/fetchDealers" if state == "All" else f"/fetchDealers/{state}"
    dealerships = get_request(endpoint)
    return JsonResponse({'dealers': dealerships}, status=200)

def get_dealer_reviews(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchReviews/dealer/{dealer_id}"
        reviews = get_request(endpoint)
        return JsonResponse({'reviews': reviews}, status=200)
    return JsonResponse({
        'message': 'Invalid dealer ID'
    }, status=400)

def get_dealer_details(request, dealer_id):
    if dealer_id:
        endpoint = f"/fetchDealer/{dealer_id}"
        dealership = get_request(endpoint)
        return JsonResponse({
            'dealer': dealership
        }, status=200)
    return JsonResponse({
        'message': 'Invalid dealer ID'
    }, status=400)

@csrf_exempt
def add_review(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            'message': 'Unauthorized'
        }, status=403)
    data = json.loads(request.body)
    post_review(data)
    return JsonResponse({
        'status': 'Review added'
    }, status=200)

def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()  # Ensure that 'initiate' is correctly defined and imported
    cars = [
        {'CarModel': model.name, 'CarMake': model.car_make.name}
        for model in CarModel.objects.select_related('car_make')
    ]
    return JsonResponse({'CarModels': cars})
