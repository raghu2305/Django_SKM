from django.shortcuts import render ,redirect , HttpResponseRedirect

from django.contrib.auth.hashers import check_password

from store.models.customer import Customer
from django.views import View
from store.views.checkout import CheckOut


class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self, request):
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_phone(phone)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                request.session['phone'] = customer.phone

                if Login.return_url:
                    if not request.META['PATH_INFO'] == Login.return_url+'/check-out':
                        return redirect('cart')
                    else:
                        return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')

            else:
                error_message = 'Invalid Phone or Password!!'
        else:
            error_message = 'Invalid Phone or Password!!'
        print(phone, password)
        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')