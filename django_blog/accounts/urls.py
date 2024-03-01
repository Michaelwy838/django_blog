from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', views.log_in, name="log_in"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.log_out, name="log_out"),
]
