from django.contrib import admin

from flower_app.models import Bouquet, Place, Consultation, Order, Composition, Category, CompositionSet


class CompositionSetInline(admin.TabularInline):
    model = CompositionSet
    extra = 1


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    inlines = [
        CompositionSetInline
    ]
    exclude = ('composition', )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
