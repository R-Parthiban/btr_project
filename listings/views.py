from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

from .choices import price_choices,state_choices,bedroom_choices
from .models import Listing


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True) # Fetches all values from listings model, in desc order of list_date and filters out to only the one's which has published as true
    
    #adding pagination
    paginator = Paginator(listings,6)# Show 6 contacts per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    #A dict to pass values to the rendered template 
    context = { 
        'listings' : paged_listings
    }

    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id) # it checks whether the page exists or not

    context = {
        'listing' : listing
    }

    return render(request,'listings/listing.html',context)

def search(request):
    #search funtionality
    queryset_list = Listing.objects.order_by('-list_date')

    #keywords field
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']  # --> This one is looking for a input field named 'keywords'
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = { 
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render(request,'listings/search.html',context)