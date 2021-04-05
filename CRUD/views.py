from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import User


# Create your views here.
def index(request):
    if request.method == 'POST':
       
        Vname = request.POST.get('urname')
        Vage = request.POST.get('urage')
        Vemail = request.POST.get('uremail')
        Vpass = request.POST.get('urpassword')

        context = User(user_name=Vname,user_age=Vage,user_email=Vemail,user_password=Vpass)
        context.save()
        

    show = User.objects.all()
    params ={'shows':show}

    #return HttpResponse("Heeloo")
    return render(request, 'crud/crudhome.html',params)

def update_data(request):
    Vid = request.GET['id']

    for data in User.objects.filter(user_id = Vid):
        upname = data.user_name
        upage = data.user_age
        upemail = data.user_email
        uppass = data.user_password
    
    uppararam = {'urname':upname,'urage':upage,'uremail':upemail,'urpassword':uppass}
    if request.method == 'POST':
        
        Rname = request.POST.get('urname')
        Rage = request.POST.get('urage')
        Remail = request.POST.get('uremail')
        Rpass = request.POST.get('urpassword')
       
        User.objects.filter(user_id = Vid).update(user_name=Rname,user_age=Rage,user_email=Remail,user_password=Rpass)
        return HttpResponseRedirect("/")
    return render(request, 'crud/crudedite.html',uppararam)



def delete_data(request):
   Vid = request.GET['id']
   User.objects.filter(user_id = Vid).delete()
   return HttpResponseRedirect('/')