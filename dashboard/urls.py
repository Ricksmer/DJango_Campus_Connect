from django.urls import path
from .views import DashboardView, AdminPanelView
from accounts.views import UpdateProfileView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('admin-panel/', AdminPanelView.as_view(), name='admin-panel'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
]
