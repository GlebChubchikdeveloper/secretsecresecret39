from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class Q1(TemplateView):
    template_name = "end2/q1.html"

class Q2(TemplateView):
    template_name = "end2/q2.html"

class Q3(TemplateView):
    template_name = "end2/q3.html"

class Q4(TemplateView):
    template_name = "end2/q4.html"

class Q5(TemplateView):
    template_name = "end2/q5.html"

class WrongAnswer(View):
    def get(self, request):
        return render(request, "end2/q1.html", {'wrong_answer': True})

class Q2WrongAnswer(View):
    def get(self, request):
        return render(request, "end2/q2.html", {'wrong_answer': True})

class Q3WrongAnswer(View):
    def get(self, request):
        return render(request, "end2/q3.html", {'wrong_answer': True})

class Q4WrongAnswer(View):
    def get(self, request):
        return render(request, "end2/q4.html", {'wrong_answer': True})

class Q5WrongAnswer(View):
    def get(self, request):
        return render(request, "end2/q5.html", {'wrong_answer': True})

class End(TemplateView):
    template_name = "end2/end.html"
