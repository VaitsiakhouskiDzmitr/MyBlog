from django import forms

class PostForm(Forms.ModelForm):
    class Meta:
        modek = Post
        fields = ['title', 'slug', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
