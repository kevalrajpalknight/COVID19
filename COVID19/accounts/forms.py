from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

#My Model
class UserCreateForm(UserCreationForm):
	class Meta():
		model = get_user_model()
		fields = ('username', 'email', 'password1', 'password2')
	def __init__(self, *agrs, **kwargs):
		super().__init__(*agrs, **kwargs)
		self.fields['username'].label = "nom d’utilisateur"
		self.fields['email'].label = "adresse E-mail"
		self.fields['password1'].label = "mot de passe"
		self.fields['password2'].label = "confirmer votre mot de passe"

class LoginForm(AuthenticationForm):
	class Meta:
		model = get_user_model()
		fields = ['username','password']
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].label = "nom d’utilisateur"
		self.fields['password'].label = "mot de passe"
		self.error_messages = {
        'invalid_login': ("Veillez entrer votre correcte %(username)s et mot de passe "
                           "Remarque : le nom d’utilisateur et le mot de passe sont des case sensitive "),
        'inactive': ("Ce compte est désactivé."),
    }