from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):

    name = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        try:
            if self.instance.pk:
                self.fields['name'].initial = self.instance.user.first_name
                self.fields['email'].initial = self.instance.user.email
        
        except Profile.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        email = self.cleaned_data.get('email', '')
        name = self.cleaned_data.get('name', '')

        self.instance.user.first_name = name
        self.instance.user.email = email

        self.instance.user.save()

        super(ProfileForm, self).save(*args, **kwargs)


    class Meta:
        model = Profile
        exclude = ('user', )
    

