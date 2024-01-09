from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from .forms import UserRegistrationForm, InventoryItemForm
from django.contrib.auth import authenticate, login
from .models import InventoryItem, Category, InventoryItemLog
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory_management.settings import LOW_QUANTITY, HIGH_QUANTITY
from django.contrib import messages

# Create your views here.
class Index(TemplateView):
    template_name = 'inventory/index.html'

class SignUp(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'inventory/signup.html', {'form':form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )

            login(request, user)
            return redirect('index')
        return render(request, 'inventory/signup.html', {'form':form})
    

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        low_inventory = InventoryItem.objects.filter(
            user = self.request.user.id,
            quantity__lte = LOW_QUANTITY
        )
        if low_inventory.count() > 0:
            if low_inventory.count() > 1:
                messages.error(request,f"{low_inventory.count()} items have low inventory")
            else:
                messages.error(request,f"{low_inventory.count()} item has low inventory")
        else:
            messages.success(request,f"All inventory items are at normal levels")

        low_inventory_ids = InventoryItem.objects.filter(
            user = self.request.user.id,
            quantity__lte = LOW_QUANTITY
        ).values_list("id", flat=True)

        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
        context = {'items':items, 'low_inventory_ids':low_inventory_ids}
        return render(request, 'inventory/dashboard.html', context)
    
class AddItem(LoginRequiredMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditItem(LoginRequiredMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('dashboard')

class DeleteItem(LoginRequiredMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventory/delete_item.html'
    success_url = reverse_lazy('dashboard')
    context_object_name='item'