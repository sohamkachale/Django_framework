from django.shortcuts import render

def landing(request):
    context = {
        "brand": "The Digitech Solutions",
        "headline": "Grow faster with AI-powered marketing",
        "subhead": "SEO, PPC, Social, Websites — all under one roof.",
        "cta_text": "Get a free audit",
    }
    return render(request, "landing.html", context)
