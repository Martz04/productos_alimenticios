from django.urls import path

from .views import \
    SearchResultsView, HomePageView, ProductCreateView, \
    ProductDetailView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('product/search', SearchResultsView.as_view(), name='product_search'),
    path('product/new', ProductCreateView.as_view(), name='product_new'),
    path('', HomePageView.as_view(), name='home')
]
