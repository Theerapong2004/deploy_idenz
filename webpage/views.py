from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'base.html')




def products(request):
    return render(request, "products.html")

def cart_view(request):
    cart = request.session.get("cart", [])  # ดึงข้อมูลจาก session
    return render(request, "cart.html", {"cart": cart})

def contact_view(request):
    return render(request, "contact.html")
from django.shortcuts import render

def add_to_cart(request, product_id):
    return render(request, "cart.html")  # ตรวจสอบว่ามี cart.html หรือไม่
