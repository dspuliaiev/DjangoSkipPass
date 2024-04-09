from django import forms
from .models import Quote, Author

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'tags', 'quote']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname']