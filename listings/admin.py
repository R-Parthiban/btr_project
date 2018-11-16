from django.contrib import admin

from .models import Listing

# Register your models here.

#this function is used to customize how the listing section in the admin console behaves 
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor') # it will display all this columns value in the listing console
    list_display_links = ('id','title') # mention the columns name, upon clicking on them we can go to that listings page
    list_filter = ('realtor',) # Provides the filter functionality to the mentioned column 
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode')
    list_per_page = 25

admin.site.register(Listing,ListingAdmin)
