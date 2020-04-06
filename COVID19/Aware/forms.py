from .models import Case
from django.forms import ModelForm

#My Model
class AddCase(ModelForm):
	class Meta():
		model = Case
		fields = "__all__"
	def __init__(self, *agrs, **kwargs):
		super().__init__(*agrs, **kwargs)
		self.fields['address'].label = "Adresse"
		self.fields['case_type'].label = "Type de boîtier"

