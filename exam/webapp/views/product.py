from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy, reverse
from webapp.models import Product
from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode


from webapp.forms import SearchForm, ProductForm

class ProductList(ListView):
    template_name = 'product/product.html'
    model = Product
    context_object_name = 'products'
    ordering = ('name')
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ProductList, self).get(request, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class ProductDetail(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreate(CreateView):
    template_name = 'product/add_product.html' 
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})


class ProductUpdate(UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'product/edit_product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.kwargs.get('pk')})


class ProductDelete(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:product_list')