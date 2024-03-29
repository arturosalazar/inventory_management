from django.urls import path
from .views import Index, SignUp, Dashboard, AddItem, EditItem, DeleteItem
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('add_item/', AddItem.as_view(), name='add_item'),
    path('edit_item/<int:pk>', EditItem.as_view(), name='edit_item'),
    path('delete_item/<int:pk>', DeleteItem.as_view(), name='delete_item'),
    path('chart_item/<int:item_id>', views.chart, name='chart_item'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
]