from django import forms
from j.models import Member

class MemberForm(forms.ModelForm):
 class Meta:
    model=Member
    fields='__all__'
