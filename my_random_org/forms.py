from django import forms


class CriteriaPasswordGenerationForm(forms.Form):
    use_nums = forms.BooleanField(initial=True, required=False)
    use_caps = forms.BooleanField(initial=False, required=False)
    use_lower = forms.BooleanField(initial=False, required=False)
    use_special_symbols = forms.BooleanField(initial=False, required=False)
    password_length = forms.IntegerField(initial=8)
