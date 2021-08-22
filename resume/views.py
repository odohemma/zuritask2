from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect



class NewResumeForm(forms.Form):
 task = forms.CharField(label="Your Name")
 priority = forms.CharField(label = "Phone Number")
 e_mail = forms.EmailField(label = "E-mail Address")
 message = forms.CharField(label="Your message", max_length=160, widget=forms.Textarea)

# Create your views here.
def index (request):
    # Check if there already exists a "resume" key in our session
    if "resume" not in request.session:
        # If not, create a new list
        request.session["resume"] = []

    
    return render(request, "resume/index.html", {
        "resume": request.session["resume"]    
    })

# Add a new task:
def message(request):
    # Check if method is POST
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewResumeForm(request.POST)
        # Check if form data is valid (server-side)
        if form.is_valid():
            # Isolate the task from the 'cleaned' version of form data
            resum = form.cleaned_data["task"]
            # Add the new task to our list of tasks
            request.session["resume"]  += [resum]
            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("resume:index"))
            
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "resume/message.html", {
                "form": form
            })

    
    return render(request, "resume/message.html", {
        "form": NewResumeForm()
    })