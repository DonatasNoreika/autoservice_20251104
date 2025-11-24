from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars/", views.cars, name="cars"),
    path("cars/<int:pk>/", views.car, name="car"),
    path("search/", views.search, name="search"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("profile/", views.ProfileUpdateView.as_view(), name="profile"),
    path("userorders/", views.UserOrderListView.as_view(), name="user_orders"),
    path("orders/", views.OrderListView.as_view(), name="orders"),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order"),
    path("orders/new/", views.OrderCreateView.as_view(), name="orders_new"),
    path("orders/<int:pk>/edit", views.OrderUpdateView.as_view(), name="orders_edit"),
    path("orders/<int:pk>/delete", views.OrderDeleteView.as_view(), name="orders_delete"),
    path("orders/<int:order_pk>/newline/", views.OrderLineCreateView.as_view(), name="orderline_new"),
    path("lines/<int:pk>/edit/", views.OrderLineUpdateView.as_view(), name="orderline_edit"),
    path("lines/<int:pk>/delete/", views.OrderLineDeleteView.as_view(), name="orderline_delete"),

]