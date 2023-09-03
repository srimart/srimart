from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    p = Product.objects.all()
   
    return render(request,'home.html',{'p':p})


def productdetails(request, pk):
    product_details = get_object_or_404(Product, id=pk)
    in_cart = False

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user, products=product_details)
        if cart_items.exists():
            in_cart = True

    return render(request, 'productdetails.html', {'productDetails': product_details, 'in_cart': in_cart})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process the form data, e.g., sending emails, saving to database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        
        return redirect('/')  # Redirect after successful form submission
    
    return render(request, 'contact.html')


def login(request):
 return render(request, 'login.html')



class CustomerRegistrationView(View):
 def get(self, request):
   form = CustomerRegistrationForm()
   return render(request, 'register.html', {'form': form})

 def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
       messages.success(request, 'congrates registeration successfull')
       form.save()
     return render(request, 'register.html', {'form': form})
 
 
@login_required
def addtocart(request, pk):
    user = request.user
    productdata = get_object_or_404(Product, id=pk)  

    cart, _ = Cart.objects.get_or_create(user=user)



    cart.products.add(productdata)

    return redirect('/cart')


@login_required
def cart(request):
    user = request.user
    carts = Cart.objects.filter(user=user)
    if not carts.exists():
        return redirect('/')
    cart = get_object_or_404(Cart, user=user)
    

    # Retrieve products in the cart and calculate total price
    products_in_cart = cart.products.all()
    total_price = sum([product.prize for product in products_in_cart])

    # Check if cart is empty
    if not products_in_cart.exists():
        return redirect('/')

    # Retrieve user details
    userDetails = Customer.objects.filter(user=user).first()

    context = {
        'cart': products_in_cart,
        'u': userDetails,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)

@login_required
def delete_cart_product(request, product_id):
    user = request.user
    cart = get_object_or_404(Cart, user=user)

    try:
        product_to_delete = Product.objects.get(id=product_id)

        cart.products.remove(product_to_delete)

    except Product.DoesNotExist:
        pass

    return redirect('cart')

@login_required
def create_customer(request):
    if request.method == 'POST':
        userDetails = Customer.objects.filter(user=request.user).first()
        form = CustomerForm(request.POST, instance=userDetails)
        if form.is_valid():
            customer = form.save(commit=False)  # Create a customer object without saving it to the database yet
            customer.user = request.user  # Assign the logged-in user to the customer's user field
            customer.save()  # Now save the customer object with the user information
            return redirect('/cart')  # Redirect to a customer list page
    else:
        userDetails = Customer.objects.filter(user=request.user).first()
        userDetail = Customer.objects.filter(user=request.user).first()
        form = CustomerForm(instance=userDetails)
    
    context = {
        'form': form,
        'u': userDetail
    }
    return render(request, 'profile.html', context)



@login_required
def deletecustomer(request, pk):
    customer = get_object_or_404(Customer, id=pk,user=request.user)
    customer.delete()
    return redirect('/profile')



@login_required
def placedorder(request):
    cartitems = Cart.objects.filter(user=request.user)
    cust = Customer.objects.filter(user=request.user).first()
    if not cust:
        return redirect('/profile')

    for cart_item in cartitems:
        # Assuming each cart item can have multiple products
        for product in cart_item.products.all():
            OrderdItems.objects.create(
                user=request.user,
                products=product,  # Use each product from the cart item
                customer=cust,
                status='ACCEPTED', 
            )

    # Step 3: Delete the cart items
    cartitems.delete()

    # Step 4: Redirect to the '/orders' page
    return redirect('/orders')

@login_required
def orderplaced(request):
   ordereditems = OrderdItems.objects.filter(user=request.user)
   totalcost = 0
   for i in ordereditems:
       if i.status != 'cancel':
        totalcost += i.products.prize
   return render(request,'orders.html',{'orderitem':ordereditems,'totalcost':totalcost})

@login_required
def cancelOrder(request,pk):
    try:
        order_item = OrderdItems.objects.get(user=request.user, id=pk)
    except OrderdItems.DoesNotExist:
        pass
    else:
        if(order_item.status != 'On the Way' or order_item.status != 'Deliverd'):
             order_item.status = 'cancel'
             order_item.save()


    return redirect('/orders')

