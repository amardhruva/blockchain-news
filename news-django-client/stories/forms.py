from django import forms

class AddNewsForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)
    image=forms.FileField()
    user_id=forms.IntegerField()
    privatekey=forms.IntegerField()
    private_n=forms.IntegerField()

class AddUserForm(forms.Form):
    userid = forms.IntegerField()
    prime1 = forms.IntegerField()
    prime2 = forms.IntegerField()