from django.shortcuts import render
from models import Post, Category

def is_valid_queryparam(param):
    return  param !='' and param is not None
def FilterView(request):
    qs = Post.objects.all()
    qs_no = Post.objects.all().count()
    qs_no = int(qs_no)
    

   
    categories = Category.objects.all()
    
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    
    if is_valid_queryparam(title_contains_query):
       qs = qs.filter(title__icontains= title_contains_query) 

    elif is_valid_queryparam(id_exact_query):
       qs = qs.filter(id= id_exact_query)  
    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(author__username__icontains=title_or_author_query ).distinct()
       
         
     
    if is_valid_queryparam(view_count_min):
       qs = qs.filter(views__gte=view_count_min)   
    if is_valid_queryparam(view_count_max):
       qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
       qs = qs.filter(post_date__gte=date_min)   
    if is_valid_queryparam(date_max):
       qs = qs.filter(post_date__lt=date_max)   
    if is_valid_queryparam(category) and category != 'Choose...':
       qs = qs.filter(category__name=category)

    
    context = {
        'queryset': qs,
        'categories': categories,
       
     
    }


    return render(request, "filterform.html", context)
