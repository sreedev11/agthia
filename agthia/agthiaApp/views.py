from django.shortcuts import render,redirect ,get_object_or_404# type: ignore
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import Local,Inter,Registration,Restaurant,Restaurant2,Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import check_password  # Import Django's password checker
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from django.views import View
from django.db import IntegrityError


def home(request):
    return render(request,'home.html')



def contacts(request):
    return render(request,'contacts.html')


def rest(request, local_id):
    restaurant = get_object_or_404(Restaurant, local_id=local_id)
    context = {'restaurant': restaurant}
    print(context)
    return render(request, 'rest.html', context)
    

def rest2(request, inter_id):
    restaurant2 = get_object_or_404(Restaurant2, inter_id=inter_id)
    context = {'restaurant2': restaurant2}
    print(context)
    return render(request, 'rest2.html', context)


def brand(request):
    local_images = Local.objects.all()
    inter_images = Inter.objects.all()
    context = {
        'local_images': local_images,
        'inter_images': inter_images
    }
    return render(request, 'brand.html', context)


def reservation_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        person = request.POST.get('person')
        timing = request.POST.get('timing')
        date = request.POST.get('date')

        subject = "New Table Reservation"
        message = f"""
        Name: {name}\n
        Email: {email}\n
        Number of People: {person}\n
        Preferred Timing: {timing}\n
        Reservation Date: {date}
        """
        from_email = 'sreedevsudhi@gmail.com'
        recipient_list = 'sreedevsudhi@gmail.com'

        send_mail(subject, message, from_email, [recipient_list], fail_silently = False)
        return redirect("home")  

    return render(request, 'home.html')


def mailus(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        text = request.POST.get('message')

        message = f"""
        Name: {name}\n
        Email: {email}\n
        Subject: {subject}\n
        Phone Number: {phone}\n
        Message: {text}\n
        """

        from_email = 'sreedevsudhi@gmail.com'
        recipient_list = 'sreedevsudhi@gmail.com'
        
        send_mail(subject, message, from_email, [recipient_list], fail_silently = False)
        return redirect("contacts/")

    return render(request,'contacts.html')

def subscribe(request):
    if request.method== 'POST':
        email = request.POST.get('email')

        message = f"""
        Email: {email}\n
        """
        subject ="New Subsciption"

        from_email = 'sreedevsudhi@gmail.com'
        recipient_list = 'sreedevsudhi@gmail.com'

        send_mail(subject, message, from_email, [recipient_list], fail_silently = False)
        return redirect("home") 

    return render(request,'home.html')


def admin_home(request):
    return render(request,'admin_home.html')

def local(request):
    return render(request,'local.html')


def inter(request):
    return render(request,'inter.html')

def upload_image(request):
    if request.method == 'POST':
        # Extract image and name from the form data
        image_file = request.FILES.get('image')
        name = request.POST.get('name', 'Default Name')  # Replace 'Default Name' with your default value if needed

        if image_file:
            # Create a new Local object with image and name
            new_local = Local(image=image_file, name=name)
            new_local.save()  # Save the object to the database
            
            # Redirect to a success page or URL
            return redirect('/local/')  # Replace '/local/' with your actual URL name
        
    # Render the upload form template for GET requests or invalid forms
    return render(request, 'local.html')


def upload_image1(request):
    if request.method == 'POST':
        # Get the uploaded image file from the form
        image_file = request.FILES.get('image')
        name = request.POST.get('name', 'Default Name')
        
        if image_file:
            new_inter = Inter.objects.create(image=image_file, name=name)
            # Optionally, you can save the instance to the database
            new_inter.save()
            
            # Redirect to a success page or wherever you want
            return redirect('/inter/')  # Replace 'upload_success' with your URL name
    return render(request, 'inter.html')

def admin_reg(request):
    return render(request,'admin_reg.html')

def register_admin(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the username or email already exists
        if Registration.objects.filter(username=username).exists() or Registration.objects.filter(email=email).exists():
            return render(request, 'admin_reg.html', {'error': 'Username or email already exists.'})

        # Hash the password
        hashed_password = make_password(password)

        # Create and save the new admin registration
        admin = Registration(name=name, username=username, email=email, password=hashed_password)
        admin.save()

        # Redirect to a success page (or any other page)
        return redirect('admin_reg')

    return render(request, 'admin_reg.htmlsr')


def login(request):
    return render(request,'login.html')



def checklogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Registration.objects.get(username=username)
            
            if check_password(password, user.password):
                return redirect('admin_home')  
            else:
                messages.error(request, 'Invalid login credentials.')

        except Registration.DoesNotExist:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')  


def image_list(request):
    local_images = Local.objects.all()
    inter_images = Inter.objects.all()
    context = {
        'local_images': local_images,
        'inter_images': inter_images
    }
    return render(request, 'image_list.html', context)



def add_restaurant(request):
    locals = Local.objects.all()
    
    if request.method == "POST":
        local_id = request.POST.get('local')
        local_instance = Local.objects.get(id=local_id)
        
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        additional_image1 = request.FILES.get('additional_image1')
        additional_image2 = request.FILES.get('additional_image2')
        additional_image3 = request.FILES.get('additional_image3')
        brand_type = request.POST.get('brand_type')
        
        restaurant = Restaurant(
            local=local_instance,
            image1=image1,
            image2=image2,
            heading=heading,
            description=description,
            additional_image1=additional_image1,
            additional_image2=additional_image2,
            additional_image3=additional_image3,
            brand_type=brand_type
        )
        restaurant.save()
        return redirect('add_rest')  # Redirect to the restaurant list after saving

    return render(request, 'add_rest.html', {'locals': locals})

def add_restaurant2(request):
    inters = Inter.objects.all()
    
    if request.method == "POST":
        inter_id = request.POST.get('inter')
        inter_instance = Inter.objects.get(id=inter_id)
        
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        heading = request.POST.get('heading')
        description = request.POST.get('description')
        additional_image1 = request.FILES.get('additional_image1')
        additional_image2 = request.FILES.get('additional_image2')
        additional_image3 = request.FILES.get('additional_image3')
        brand_type = request.POST.get('brand_type')
        
        restaurant2 = Restaurant2(
            inter=inter_instance,
            image1=image1,
            image2=image2,
            heading=heading,
            description=description,
            additional_image1=additional_image1,
            additional_image2=additional_image2,
            additional_image3=additional_image3,
            brand_type=brand_type
        )
        restaurant2.save()
        return redirect('add_rest2')  

    return render(request, 'add_rest2.html', {'inter': inters})
       


def add_rest(request):
    locals = Local.objects.all()
    return render(request, 'add_rest.html', {'locals': locals})


def add_rest2(request):
    inters = Inter.objects.all()
    return render(request, 'add_rest2.html', {'inters': inters})

def add_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        profile_photo = request.FILES.get('profile_photo')

        if Profile.objects.filter(email=email).exists():
            # Email already exists
            return render(request, 'add_profile.html', {'error': 'Email already exists. Please use a different email address.'})

        profile = Profile(
            name=name,
            phone=phone,
            email=email,
            address=address,
            profile_photo=profile_photo
        )

        try:
            profile.save()
            return render(request, 'add_profile.html', {'success': 'Profile added successfully.'})
        except IntegrityError:
            return render(request, 'add_profile.html', {'error': 'An error occurred while adding the profile. Please try again.'})
    return render(request, 'add_profile.html')

def profile_view(request):
    profiles = Profile.objects.all()  # Assuming you have a Profile model with 'name', 'phone', 'email', 'address', and 'profile_photo' fields
    return render(request, 'profile.html', {'profiles': profiles})

def edit_profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'edit_profile.html', {'profile': profile})

def save_profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.phone = request.POST['phone']
        profile.email = request.POST['email']
        profile.address = request.POST['address']
        if 'profile_photo' in request.FILES:
            profile.profile_photo = request.FILES['profile_photo']
        profile.save()
        return redirect('profile-view')
    return render(request, 'edit_profile.html', {'profile': profile})

