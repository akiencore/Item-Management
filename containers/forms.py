from django import forms
from .models import Container, Item


MAX_NAME_LENGTH = 50
MAX_COLOR_LENGTH = 20

class ContainerForm(forms.ModelForm):
    class Meta:
        model = Container
        fields = ['name', 'length', 'width', 'height', 'color', 'purpose', 'note']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > MAX_NAME_LENGTH:
            raise forms.ValidationError("This name is too long")
        if len(name) == 0:
            raise forms.ValidationError("Name cannot be blank")
        return name

    def clean_color(self):
        color = self.cleaned_data.get("color")
        if len(color) > MAX_COLOR_LENGTH:
            raise forms.ValidationError("This color is too long")
        if len(color) == 0:
            raise forms.ValidationError("Color cannot be blank")
        return color

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'length', 'width', 'height', 'color', 'category', 'in_container', 'purpose', 'note']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) > MAX_NAME_LENGTH:
            raise forms.ValidationError("This name is too long")
        if len(name) == 0:
            raise forms.ValidationError("Name cannot be blank")
        return name

    def clean_color(self):
        color = self.cleaned_data.get("color")
        if len(color) > MAX_COLOR_LENGTH:
            raise forms.ValidationError("This color is too long")
        if len(color) == 0:
            raise forms.ValidationError("Color cannot be blank")
        return color