from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    # readonly_fields=("create_date",)
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock", )
    list_display_links = ("create_date", )
    search_fields = ("name", "create_date")
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 10
    ordering = ("name",)
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock")
    fieldsets = (
        ("General fields", {
            "fields": (
                ('name', 'slug'), "is_in_stock" # to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            # "classes" : ("collapse", ),
            "fields" : ("description",),
            'description' : "You can use this section for optionals settings"
        })
    )







admin.site.register(Product, ProductAdmin)


admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"