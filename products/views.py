from django.shortcuts import render, get_object_or_404 , redirect
from django.contrib import messages
from .models import Product, Category, Color, Discount , Order
from .forms import CommentForm
from django.views import View
from django.views import generic
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from .models import Product, Category, Color
from .forms import CommentForm


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # محاسبه قیمت با تخفیف برای هر محصول
        for product in context['products']:
            if product.discount:
                discount = product.discount.discount
                product.discount_price = int(product.price - (product.price * discount / 100))
            else:
                product.discount_price = int(product.price)
        return context





def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    # دریافت نظرات محصول
    product_comment = product.comments.filter(active=True).order_by('-datetime_created')
    
    # دسته‌بندی‌ها و رنگ‌های مرتبط با محصول
    category_product = Category.objects.filter(products=product)
    color_product = Color.objects.filter(products=product)
    
    # محاسبه قیمت تخفیف‌دار
    discount_price = product.get_discount_price()

    # بررسی فرم نظرات
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, _('Comment Successfully created'))

            # بازنشانی فرم نظرات پس از ذخیره موفقیت‌آمیز
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request, 
        'products/product_detail.html', 
        {
            'product': product,
            'comment_form': comment_form,
            'product_comment': product_comment,
            'category': category_product,
            'colors': color_product,
            'discount_price': discount_price,  
        }
    )


@login_required
def create_order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        total_price = product.price * quantity
        order = Order.objects.create(
            user=request.user,
            product=product,
            quantity=quantity,
            total_price=total_price
        )
        
        return redirect('product-detail')
    return redirect('product-detail')

@login_required
def user_orders(request):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'products/user_orders.html', {'orders': orders})


def product_search(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Product.objects.filter(title__icontains=query)  # جستجو بر اساس نام محصول
    return render(request, 'products/product_search.html', {'results': results, 'query': query})

