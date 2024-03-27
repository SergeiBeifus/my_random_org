from django.shortcuts import render
from .utils import PasswordGenerator
from my_random_org.forms import CriteriaPasswordGenerationForm


# Create your views here.
def index(request):
    passwords = []
    form = CriteriaPasswordGenerationForm()
    if request.method == 'POST':
        form = CriteriaPasswordGenerationForm(request.POST)
        if form.is_valid():
            password_generator = PasswordGenerator(
                password_length=form.cleaned_data['password_length'],
                use_upper=form.cleaned_data['use_caps'],
                use_lower=form.cleaned_data['use_lower'],
                use_numbers=form.cleaned_data['use_nums'],
                use_special_symbols=form.cleaned_data['use_special_symbols']
            )
            passwords = [password_generator.generate() for _ in range(8)]
    return render(request, 'generate_password/index.html', context={'form': form, 'passwords': passwords})
