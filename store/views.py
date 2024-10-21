from django.shortcuts import get_object_or_404, redirect, render

from store.models import Product

# Create your views here.

def home(request):
    return render(request, 'base.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def userdashboard(request):
    return render(request, 'userdashboard.html')
def login(request):
    
    if request.method == 'POST':
        # handle login logic
        # if successful:
        return redirect('userdashboard')  # Redirect to user dashboard after login
    return render(request, 'login.html')
   
def categories(request):
    return render(request, 'categories.html')
def cat_type(request):
    return render(request, 'cat_type.html')
def signup(request):
    return render(request, 'signup.html')
def orders(request):
    return render(request, 'orders.html')
def logout_user(request):
    # auth_logout(request)
    # return redirect('home')
    return render(request, 'logout_user.html')
def review_dashboard(request):
    return render(request, 'review_dashboard.html')
def products(request):
    return render(request, 'products.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def tracking(request):
    return render(request, 'tracking.html')
def product_list(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Fetch the product by ID
    return render(request, 'products/product_detail.html', {'product': product})
