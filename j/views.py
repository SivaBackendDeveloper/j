from django.contrib import messages, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from .filters import MemberFilter


from j.forms import MemberForm
from j.models import Member


def show_view(request):
   members=Member.objects.all()

   myFilter=MemberFilter(request.GET,queryset=members)
   members=myFilter.qs

   return render(request, 'j/index.html',{'members':members,'myFilter':myFilter})

@login_required()
def insert_view(request):
   form=MemberForm()
   if request.method == 'POST':
    form = MemberForm(request.POST)
    if form.is_valid():
       form.save()
    return redirect('/')
   return render(request, 'j/insert.html', {'form': form})


@login_required()
def delete_view(request, id):
  member = Member.objects.get(id=id)
  member.delete()
  return redirect('/')


@login_required()
def update_view(request,id):
   member = Member.objects.get(id=id)
   if request.method == 'POST':
     form = MemberForm(request.POST, instance=member)
     if form.is_valid():
        form.save()
     return redirect('/')
   return render(request, 'j/update.html', {'member': member})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "registration/login.html",
                    context={"form":form})

def logout_view(request):
    auth.logout(request)
    return redirect('/')


