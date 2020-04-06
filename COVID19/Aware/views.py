# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views import  generic
from . import models
from django.contrib import messages
from . import forms
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from .models import Case, Location
from django.db.models import Count
User = get_user_model()

# Create your views here.
class CaseList(generic.ListView):
    model = models.Case
    template_name = 'Case/Case_list.html'
    queryset = {"Cases":Case.objects.all().values('address', 'case_type').annotate(total=Count('address')).order_by('address','total','case_type'),}


class CreateCase(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.Case
    template_name = 'Case/Case_form.html'
    form_class = forms.AddCase
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Case
    select_related = ('user',)
    success_url = reverse_lazy('case:all')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Case Deleted')
        return super().delete(*args, **kwargs)
		