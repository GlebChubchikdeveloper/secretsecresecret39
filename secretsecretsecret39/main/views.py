from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "main/index.html"

class Hint(TemplateView):
    template_name = "hint/index.html"

class Wrong(TemplateView):
    template_name = "wrong/index.html"

class Next(View):
    def post(self, request):
        code = request.POST.get("code")
        if code == "Xf3320aaE":
            return redirect("/end1")
        elif code == "D46eC1739":
            return redirect("/end2")
        elif code == "dlo93y3891":
            return redirect("/end3")
        else:
            return render(request, "main/index.html", {'wrong_code': True})