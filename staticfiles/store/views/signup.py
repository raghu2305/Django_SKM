from django.shortcuts import render, redirect

from django.contrib.auth.hashers import make_password

from store.models.customer import Customer
from django.views import View


def validateCustomer(customer):
    error_message = None
    if (not customer.first_name):
        error_message = "First Name Required!!"
    elif len(customer.first_name) < 2:
        error_message = "First Name must be atleast 2 character long"
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Invalid Phone Number'
    elif len(customer.phone) > 13:
        error_message = 'Invalid Phone Number'
    elif len(customer.password) < 8:
        error_message = 'Password must be atleast 8 character long.'
    elif customer.isExists():
        error_message = 'Email Already Registered.'
    elif customer.isExists_phone():
        error_message = 'Phone Number Already Registered.'

    return error_message


def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
    # validation
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }
    error_message = None

    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
    error_message = validateCustomer(customer)

    # saving
    if not error_message:
        print(first_name, last_name, phone, email, password)
        customer.password = make_password(customer.password)
        customer.register()
        return redirect('homepage')
    else:
        data = {
            'error': error_message,
            'values': value
        }
        return render(request, 'signup.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
