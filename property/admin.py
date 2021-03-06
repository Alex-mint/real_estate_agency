from django.contrib import admin

from .models import Flat, Claim, Owner

class OwnerInline(admin.TabularInline):
    model = Flat.flat_owners.through
    raw_id_fields = ['owner']

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields =('liked_by',)
    inlines = [OwnerInline]

class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'flat',)
    list_display = ('text',)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owner_phonenumber',
                    'owner_pure_phonenumber',)
    raw_id_fields = ('flat',)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
