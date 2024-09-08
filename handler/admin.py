from django.contrib import admin
from .models import (
    Company,
    Category,
    Image,
    Product,
    ContactUs,
    Purchase,
    CustomPurchase,
    ListedProduct,
    ListedProductPurchase
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "logo", "overview")
    search_fields = ("name",)

    def has_add_permission(self, request):
        """
        Restrict adding new instances if one already exists.
        """
        # Allow adding if no instances exist; otherwise, deny.
        if Company.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        """
        Allow changing if an instance exists; otherwise, deny.
        """
        if not Company.objects.exists() and not obj:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        """
        Optionally restrict deletion if needed.
        """
        return False  # Disable delete permissions if needed

    def get_queryset(self, request):
        """
        Restrict the queryset to show only the existing instance.
        """
        qs = super().get_queryset(request)
        if not Company.objects.exists():
            return qs.none()  # Hide all instances if none exist
        return qs


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "rating")
    search_fields = ("name", "description")
    list_filter = ("category",)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("name", "product")
    search_fields = ("name",)
    list_filter = ("product",)


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")
    search_fields = ("name", "email", "message")
    list_filter = ("email",)

    def has_add_permission(self, request):
        # Disable the 'Add' button
        return False


@admin.register(Purchase)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("purchase_number", "product", "user", "notes")
    search_fields = ("name", "product", "purchase_number")
    list_filter = ("purchase_number",)

    def has_add_permission(self, request):
        # Disable the 'Add' button
        return False

@admin.register(ListedProductPurchase)
class ListedProductPurchaseAdmin(admin.ModelAdmin):
    list_display = ("purchase_number", "product", "user", "notes")
    search_fields = ("name", "product", "purchase_number")
    list_filter = ("purchase_number",)

    def has_add_permission(self, request):
        # Disable the 'Add' button
        return False


@admin.register(CustomPurchase)
class CustomProductAdmin(admin.ModelAdmin):
    list_display = ("purchase_number", "product_image", "user", "notes")
    search_fields = ("user", "purchase_number")
    list_filter = ("purchase_number",)

    def has_add_permission(self, request):
        # Disable the 'Add' button
        return False

@admin.register(ListedProduct)
class ListedProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "category", "availability", "condition")
    search_fields = ("title", "category__name")
    list_filter = ("availability", "category", "condition")

    def has_add_permission(self, request):
        return False

    def get_readonly_fields(self, request, obj=None):  # Added obj=None
        if request.user.is_superuser:
            return []
        return ('title', 'price', 'category', 'availability', 'condition')