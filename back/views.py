from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.http import  HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from back.models import Product, Category, Customer, Contact
def index(request):
    product =  Product.objects.all()
    category = Category.objects.all()
    context = {
        'index': product,
        'cat': category,
    }
    return render(request, 'index.html', context)

def home(request):
    product = Product.objects.all()
    category = Category.objects.all()
    # customer = Customer.object.all()
    context = {
        'index': product,
        'cat': category,
        # 'user': customer,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')


def recipes(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'cat': category,
        'index': product,
    }
    return render(request, 'recipes.html', context)


def recipe(request,id):
    category = Category.objects.all()
    prod = Product.objects.filter(id=id).first()
    print(prod)
    # product=prod.Category.all()
    # print(product)
    context = {
        'cat': category,
        'prod': prod,
        # 'product': product
    }
    return render(request, 'recipe.html', context)


# s..recipe

def template(request, id):
    category = Category.objects.filter(id=id).first()
    prod = Product.objects.filter(id=category.id).first()
    context = {
        'cat': category,
        'prod': prod,
    }

    return render(request, 'template.html', context)


def tags(request):
    category = Category.objects.all()
    context = {
        'cat': category,
    }
    return render(request, 'tags.html', context)

def contact(request):
    return render(request, 'contact.html')


class signup(View):
    def get(self,request):
        return render(request, 'signup.html')

    def post(self,request):
        postData = request.POST
        f_name = postData.get('firstname')
        l_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': f_name,
            'last_name': l_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        register = Customer(first_name = f_name,
                            last_name= l_name,
                            phone=phone,
                            email = email,
                            password = password)
        #copy
        error_message = self.validateCustomer(register)

        if not error_message:
            print(f_name, l_name, phone, email, password)
            register.password = make_password(register.password)
            register.save()
            return redirect('/login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'


        return error_message


        register.password = make_password(register.password)
        register.registerData()
        return render(request, 'login.html')

# class login(View):
#     def get(self, request):
#         return render(request, 'login.html')
#
#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         register = Customer.get_customer_by_email(email)
#         error_message = None
#         try:
#             if register:
#                 flag = check_password(password, register.password)
#                 if flag:
#                     email=Customer(email=email)
#                     if email:
#                         request.sesion['name'] = register.name
#                         request.sesion['email'] = register.email
#                         Display_id = request.sesion.get('register_id')
#                         Display_name = request.sesion.get('name')
#                         context={
#                             'data': Display_id,
#                             'data_id': Display_name
#                     }
#                 return render(request,'home.html')
#
#
#             else:
#                 return render(request, 'login.html')
#
#         except Exception:
#             return HttpResponse("This email does not exist")
class login(View):
    return_url = None
    def get(self , request):
        login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:

                if login.return_url:
                    return HttpResponseRedirect(login.return_url)
                else:
                    print()
                    request.session['user'] = customer.first_name
                    login.return_url = None
                    return redirect('/')

            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('/login')
    return redirect('/login')
    # request.sesion.clear()
    # return redirect('login')

# @login_required
def search(request):
    data = request.POST.get('search')
    context = Product.objects.filter(Q(name__icontains=data) | Q(description__icontains=data) | Q(time__icontains=data))
    return render(request,'search.html',{'context': context})


