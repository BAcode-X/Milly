from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'w3-input w3-hover-border-cyan',
                                    'placeholder':'Name'}),required=True, max_length=100)
    Email = forms.EmailField(widget=forms.EmailInput(
                        attrs={
                                'class':'w3-input w3-hover-border-cyan',
                                'placeholder':'Email'}),required=True)
    Subject = forms.CharField(widget=forms.TextInput(
                                attrs={
                                    'class':'w3-input w3-hover-border-cyan',
                                    'placeholder':'Subject'}),required=True)
    Comment = forms.CharField(widget=forms.Textarea(
                                attrs={
                                    'class':'w3-input w3-hover-border-cyan',
                                    'placeholder':'Message'}) , required=True)