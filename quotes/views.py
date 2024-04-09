from django.shortcuts import render, redirect
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm
from .connect import get_mongodb

def main(request):
    db = get_mongodb()
    mongo_quotes = db.quotes.find()
    quotes = [quote for quote in mongo_quotes]
    return render(request, 'quotes/index.html', context={'quotes': quotes})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = AuthorForm()
    return render(request, 'add_author.html', {'form': form})

def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = QuoteForm()
    return render(request, 'add_quote.html', {'form': form})