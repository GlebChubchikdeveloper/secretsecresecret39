from django.urls import path
from . import views

urlpatterns = [
    path("", views.Q1.as_view(), name="q1"),
    path("/q2", views.Q2.as_view(), name="q2"),
    path("/q3", views.Q3.as_view(), name="q3"),
    path("/q4", views.Q4.as_view(), name="q4"),
    path("/q5", views.Q5.as_view(), name="q5"),
    path("/wrong_answer", views.WrongAnswer.as_view(), name="wrong_answer"),
    path("/q2/wrong_answer", views.Q2WrongAnswer.as_view(), name="q2wrong_answer"),
    path("/q3/wrong_answer", views.Q3WrongAnswer.as_view(), name="q3wrong_answer"),
    path("/q4/wrong_answer", views.Q4WrongAnswer.as_view(), name="q4wrong_answer"),
    path("/q5/wrong_answer", views.Q5WrongAnswer.as_view(), name="q5wrong_answer"),
    path("/end", views.End.as_view(), name="end"),
]