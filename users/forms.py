from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    # Явно объявляем поля, которые хотим добавить

    username = forms.CharField(
        label='Логин',
        help_text=('Обязательное поле. Не более 150 символов. Только буквы, цифры и @/./+/-/_.'),
        error_messages={
            'unique': ("Пользователь с таким именем уже существует."),
        },
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=64,
        help_text='Введите действующий адрес электронной почты.',
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    first_name = forms.CharField(
        max_length=32,
        label='Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'})
    )
    last_name = forms.CharField(
        max_length=32,
        label='Фамилия',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'})
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password'  # Помогает браузерам не заполнять поле автоматически
        }),
        help_text=(
            "<ul>"
            "<li>Ваш пароль не должен содержать ваше имя или другую личную информацию.</li>"
            "<li>Ваш пароль должен содержать как минимум 8 символов.</li>"
            "<li>Ваш пароль не может быть одним из широко распространённых паролей.</li>"
            "<li>Ваш пароль не может состоять только из цифр.</li>"
            "</ul>"
        )
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password'
        }),
        help_text="Введите тот же пароль, что и выше, для проверки."
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # Указываем поля для отображения в форме, включая стандартные и добавленные
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)
        # Опционально: можно переопределить виджеты для стандартных полей через Meta.widgets
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),

        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'})
        }
  
    # При необходимости можно добавить пользовательскую валидацию
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже существует.")
        return email