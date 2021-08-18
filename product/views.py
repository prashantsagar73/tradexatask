from django.shortcuts import render
from .models import Product
from math import ceil
from django.views.generic import DetailView

# Create your views here.
# index page
def index(request):
    return render(request,"index.html")

# product home
def home(request):
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
            prod = Product.objects.filter(category=cat)
            n = len(prod)
            nSlide = n // 4 + ceil((n // 4) - (n // 4))
            allprods.append([prod, range(1, nSlide), nSlide])
    prashant = {'allprods': allprods}
    return render(request,'product/home.html', prashant)

# productdetals views
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/productview.html'