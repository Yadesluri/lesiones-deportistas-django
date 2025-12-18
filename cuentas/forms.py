from django import forms
from django.contrib.auth.models import User, Group

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    grupo = forms.ModelChoiceField(
        queryset=Group.objects.filter(name__in=['entrenadores', 'kinesiologos']),
        required=True,
        label="Rol en el sistema",
        empty_label="Seleccione un rol"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'grupo']

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return p2
