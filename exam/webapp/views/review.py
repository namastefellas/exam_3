from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy, reverse
from webapp.models import Review
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.forms import ReviewForm

class ReviewCreate(CreateView):
    pass