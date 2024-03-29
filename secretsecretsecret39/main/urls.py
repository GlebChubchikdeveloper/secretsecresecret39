from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("next", views.Next.as_view(), name="next"),
    path("hint", views.Hint.as_view(), name="hint"),
    path("wrong", views.Wrong.as_view(), name="wrong"),
]