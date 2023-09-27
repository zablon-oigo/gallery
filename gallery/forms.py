from django import forms 
from .models import Photo

INPUT_CLASSES='border border-gray-600 rounded-lg px-6 py-4 w-full'
class AddPhoto(forms.ModelForm):
    class Meta:
        model=Photo
        fields=['category','name','image','description',]
        widgets={
            'category':forms.Select(attrs={
                'placeholder':'select the category the image belongs',
                'class':INPUT_CLASSES

            }),
            'name':forms.TextInput(attrs={
                'placholder':'Enter a name for the image',
                'class':INPUT_CLASSES

            }),
            'image':forms.ClearableFileInput(attrs={
                'class':'w-full py-3 px-4 border border-gray-600 rounded-lg'

            }),
            'description':forms.Textarea(attrs={
                'placeholder':'write description about the image  here...',
                'class':'border border-gray-600 rounded-lg h-48 w-full px-6 py-4'

            })
        }
    
    