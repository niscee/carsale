from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Image,
    Product,
    Category,
    Company,
    Purchase,
    CustomPurchase,
    ListedProduct,
    ListedProductPurchase,
)
from .forms.contact import ContactForm
from .forms.purchase import PurchaseForm, CustomPurchaseForm, ListedProductPurchaseForm
from .forms.listing_product import ListedProductForm
from .forms.auth import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def home_view(request):
    query = request.GET.get("q")
    products = Product.objects.all().order_by("price")
    listed_products = ListedProduct.objects.all().order_by("price")

    if query:
        products = products.filter(name__icontains=query)

    image = Image.objects.latest("id")
    categories = Category.objects.all()
    company = Company.objects.latest("id")

    return render(
        request,
        "home.html",
        {
            "image": image,
            "products": products,
            "categories": categories,
            "company": company,
            "query": query,
            "listed_products": listed_products,
        },
    )


def about_view(request):
    company = Company.objects.latest("id")
    return render(request, "about.html", {"company": company})


def media_view(request):
    products = Product.objects.all().order_by("price")
    company = Company.objects.latest("id")

    # Pass images to the template context
    return render(
        request,
        "media.html",
        {
            "products": products,
            "company": company,
        },
    )


def listed_item_view(request):
    products = ListedProduct.objects.all().order_by("price")
    company = Company.objects.latest("id")

    # Pass images to the template context
    return render(
        request,
        "listed_items.html",
        {
            "products": products,
            "company": company,
        },
    )


def contact_view(request):
    company = Company.objects.latest("id")
    context = {
        "company": company,
    }
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!!!!!!")
            return redirect("contact")
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = ContactForm()
        context["form"] = form

    return render(request, "contact.html", context)


def register_view(request):
    company = Company.objects.latest("id")
    context = {
        "company": company,
    }
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")  # Redirect to a success page
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = RegisterForm()

    context["form"] = form
    return render(request, "register.html", context)


def login_view(request):
    company = Company.objects.latest("id")
    context = {
        "company": company,
    }
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    context["form"] = form
    return render(request, "login.html", context)


def search_view(request):
    query = request.GET.get("q", "")
    # Implement search logic here
    return render(request, "search_results.html", {"query": query})


def item_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    company = Company.objects.latest("id")
    context = {
        "product": product,
        "company": company,
    }
    return render(request, "individual_item.html", context)


def listed_item_detail_view(request, id):
    product = get_object_or_404(ListedProduct, id=id)
    company = Company.objects.latest("id")
    context = {
        "product": product,
        "company": company,
    }
    return render(request, "individual_listed_item.html", context)


@login_required
def dashboard_view(request):
    company = Company.objects.latest("id")
    user = request.user
    products = Purchase.objects.filter(user_id=user)
    custom_products = CustomPurchase.objects.filter(user_id=user)
    listed_products = ListedProduct.objects.filter(user=user)
    listed_products_purchase = ListedProductPurchase.objects.filter(user=user)

    purchases = []
    for product in products:
        purchases.append(product)

    for custom in custom_products:
        purchases.append(custom)

    for listed_product in listed_products_purchase:
        purchases.append(listed_product)

    context = {
        "company": company,
        "user": request.user,
        "purchases": purchases,
        "listed_products": listed_products,
    }
    return render(request, "dashboard.html", context)


def logout_view(request):
    logout(request)  # Logs out the user
    return redirect("home")


def purchase_view(request, id):
    product = get_object_or_404(Product, id=id)
    company = Company.objects.latest("id")
    user = request.user

    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = PurchaseForm(initial={"product": product, "user": user})

    context = {
        "product": product,
        "company": company,
        "form": form,
    }
    return render(request, "purchase.html", context)


def listed_item_purchase_view(request, id):
    product = get_object_or_404(ListedProduct, id=id)
    company = Company.objects.latest("id")
    user = request.user

    if request.method == "POST":
        form = ListedProductPurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ListedProductPurchaseForm(initial={"product": product, "user": user})

    context = {
        "product": product,
        "company": company,
        "form": form,
    }
    return render(request, "listed_item_purchase.html", context)


def listed_item_delete_view(request, id):
    product = get_object_or_404(ListedProduct, id=id)
    product.delete()
    return redirect("dashboard")


def custom_purchase_view(request):
    context = {}
    user = request.user
    if request.method == "POST":
        form = CustomPurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_valid():
                form.save()
                messages.success(request, "Purchase successful!!!!")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = CustomPurchaseForm(initial={"user": user})

    context["form"] = form
    return render(request, "custom_dashboard_purchase.html", context)


def create_listing_view(request):
    context = {}
    user = request.user
    if request.method == "POST":
        form = ListedProductForm(request.POST, request.FILES)
        if form.is_valid():
            if form.is_valid():
                form.save()
                messages.success(request, "Added successful!!!!")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = ListedProductForm(initial={"user": user})

    context["form"] = form
    return render(request, "create_listing_dashboard.html", context)


def success_view(request):
    company = Company.objects.latest("id")
    context = {
        "company": company,
    }
    return render(request, "success.html", context)
