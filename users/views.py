""" from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied 

from .forms import ApplicantProfileForm
from .models import Applicant,Customuser



def create_applicant(request,pk):
    user = Customuser.objects.get(pk=pk)
    user_form = ApplicantProfileForm(instance=user)
    ProfileInlineFormset = inlineformset_factory(Customuser,Applicant,fields=('name','birth_date','phone','country','city'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = ApplicantProfileForm(request.POST,instance=user)
            formset = ProfileInlineFormset(request.POST,instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST,instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('')
        return render(request,"",){
            "noodle" : pk,
            "noodle_form": user_form,
            "formset": formset,

        }
   else:
       raise PermissionDenied

 """