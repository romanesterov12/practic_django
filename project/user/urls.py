from django.urls import path
from user.views import AuthView


urlpatterns = [
    path('register/', AuthView.as_view()),
]
