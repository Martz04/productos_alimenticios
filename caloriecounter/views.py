from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Product

class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(title__icontains=query)
        return object_list


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'new_product.html'
    fields = ["title", "kcalorie", "carbs", "fat", "protein", "sodium"]


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit.html'   
    fields = ["title", "kcalorie", "carbs", "fat", "protein", "sodium"]


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'   
    success_url = reverse_lazy('home')