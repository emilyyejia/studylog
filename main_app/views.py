from django.shortcuts import render
class Item:
    def __init__(self, name, category, country, currency, price_local, price_cad):
        self.name = name
        self.category = category
        self.country = country
        self.currency = currency
        self.price_local = price_local
        self.price_cad = price_cad

usd_to_cad = 1.35
cny_to_cad = 0.19

items = [
    Item("Big Mac", "Food", "Canada", "CAD", 6.77, 6.77),
    Item("Big Mac", "Food", "United States", "USD", 5.66, round(5.66 * usd_to_cad, 2)),
    Item("Big Mac", "Food", "China", "CNY", 21.00, round(21.00 * cny_to_cad, 2)),

    Item("Air Force One Nike", "Footwear", "Canada", "CAD", 160.00, 160.00),
    Item("Air Force One Nike", "Footwear", "United States", "USD", 150.00, round(150.00 * usd_to_cad, 2)),
    Item("Air Force One Nike", "Footwear", "China", "CNY", 1100.00, round(1100.00 * cny_to_cad, 2)),
]

# Create your views here.
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
def price_index(request):
    return render(request, 'index.html', { 'items': items})