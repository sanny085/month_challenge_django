from django.urls import path
from . import views

urlpatterns = [
    # path('january/', views.january),
    # path('february', views.february),
    path("", views.display_tabular_month),
    path('<int:month>', views.monthly_challenges_by_number),
    path('<str:month>', views.monthly_challenges, name="month_challenge")

]
