import uuid
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    logo = models.ImageField(upload_to="company_logos/", blank=True, null=True)
    slider = models.ImageField(upload_to="slider/", blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)

    facebook_link = models.URLField(max_length=255, blank=True, null=True)
    twitter_link = models.URLField(max_length=255, blank=True, null=True)
    instagram_link = models.URLField(max_length=255, blank=True, null=True)

    # Terms and Conditions
    terms_and_conditions = models.TextField(
        default="Please read our terms and conditions carefully before using our services."
    )

    class Meta:
        verbose_name = "Company details"
        verbose_name_plural = "Company details"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/")
    description = models.TextField()
    rating = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="product_images/")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        verbose_name = "Product images"
        verbose_name_plural = "Product images"

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"

    def __str__(self):
        return f"{self.name} - {self.email}"


class Purchase(models.Model):
    purchase_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Purchase by {self.user.username} of {self.product.name}"


class CustomPurchase(models.Model):
    purchase_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_image = models.ImageField(
        upload_to="custom_product/", blank=True, null=True
    )
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Custom purchase: {self.purchase_number}"


class ListedProduct(models.Model):
    CONDITION_NEW = 'new'
    CONDITION_USED = 'used'
    CONDITION_REFURBISHED = 'refurbished'

    CONDITION_CHOICES = [
        (CONDITION_NEW, 'New'),
        (CONDITION_USED, 'Used'),
        (CONDITION_REFURBISHED, 'Refurbished'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="listed_products/")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="listed_products"
    )
    availability = models.BooleanField(default=True)
    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default=CONDITION_NEW
    )

    def __str__(self):
        return self.title


class ListedProductPurchase(models.Model):
    purchase_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(ListedProduct, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Purchase by {self.user.username} of {self.product.title}"