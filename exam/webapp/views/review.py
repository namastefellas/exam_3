from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy, reverse
from webapp.models import Review, Product
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import ReviewForm

class ReviewCreate(CreateView):
    template_name = 'review/create.html'
    form_class = ReviewForm
    model = Review
    # permission_required = 'review.add_review'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.product = product
        review.author = self.request.user
        review.save()
        return redirect('webapp:product_view', pk=self.kwargs.get('pk'))



class ReviewUpdate(UpdateView):
    form_class = ReviewForm
    model = Review
    template_name = 'review/edit.html'
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.kwargs.get('pk')})


class ReviewDelete(DeleteView):
    model = Review
    template_name = 'review/delete.html'
    context_object_name = 'review'
    success_url = reverse_lazy('webapp:product_list')