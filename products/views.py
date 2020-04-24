from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    # I will add that to the context so our products will be available in the template.
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
