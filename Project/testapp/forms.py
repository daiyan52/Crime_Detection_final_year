from django.forms import ModelForm
from testapp.models import User,Profile,VideoData
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1','password2',]


class VideoDataForm(ModelForm):
    class Meta:
        model = VideoData
        fields = ['video_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video_file'].widget.attrs.update({'class': 'file-field input-field'})

