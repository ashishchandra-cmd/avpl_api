from django.db import models
from home.models import *
from django.db import models
from django.conf import settings
from django.contrib.admin import AdminSite
from Apps.Vendor.models import *
from home.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

COMPLAIN_CHOICE=(
    ('P','Product'),
    ('D','Delivery'),
    ('O','Other')
)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
        #######signal for token####
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance, created, **kwargs):
        if created:
            Token.objects.create(user=instance)
    def __str__(self):
        return self.user.username

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    county = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Addresses'

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.quantity}-quantity add into cart {self.item}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        if self.item.discount_price:
            return self.quantity * self.item.discount_price
        else:
            return None

    def get_amount_saved(self):
        if self.get_total_discount_item_price():
            return self.get_total_item_price() - self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()
    def get_final_price(self):
        if self.get_total_discount_item_price():
            return self.get_total_item_price() - self.get_total_discount_item_price()
        else:
            return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    Payment = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(AddressShop, related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    address=models.CharField(max_length=300)
    address2=models.CharField(max_length=300)
    zipcode=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)
    shipped = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_amount_saved()
            print(order_item.get_amount_saved())
            #print(total)
        return total
    def shipped_status(self):
        if self.Payment==True and self.shipped==True:
            return True
        else:
            return False
    def reduce_quantity(self):
        pass


class Complain(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE, default="not about product")
    complain_relation_to=models.CharField(max_length=1,choices=COMPLAIN_CHOICE)
    complain=models.TextField(max_length=100)

    def __str__(self):
        return f"complain of {self.product} is {self.complain}"

class UserOTP(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_st=models.DateTimeField(auto_now=True)
    otp=models.CharField(max_length=10, default='N/A')
    otp_mobile=models.CharField(max_length=10, default="N/A")

    
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class InvoiceData(models.Model):
    product_details = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_info = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order_details = models.ForeignKey(Order, on_delete=models.CASCADE)
    invoie = models.FileField(upload_to='Apps/user/invoice')

    def __int__(self):
        return self.id
        
        
        from rest_framework import serializers
from home.models import *
from .models import *
from django.contrib.auth.models import Group,Permission

#Home Model view set

class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','is_user')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

class ProducttableSerializer(serializers.ModelSerializer):
    category=CategorySerializer
    class Meta:
        model = Product
        fields = ('id','title','price','description','category','brand_name','discount_percent','image','max_price','hsn_number')

class SubcategorySerializer(serializers.ModelSerializer):
    category=CategorySerializer
    class Meta:
        model=SubCategory
        fields="__all__"

class BrandSerializer(serializers.ModelSerializer):
    sub_category=SubcategorySerializer
    class Meta:
        model=Brand
        fields="__all__"

#------------------------------------------------------------

# userapp model api

class UserProfileSerializer(serializers.ModelSerializer):
    user=CustomUserSerializer
    class Meta:
        model=UserProfile
        fields="__all__"

# class OrderItemSerializer(serializers.ModelSerializer):
#     user=CustomUserSerializer
#     item=store_productSerializer
#     store=StoreSerializer
#     class Meta:
#         model=OrderItem
#         fields= ['user','item','store','quantity']


# class OrderSerializer(serializers.ModelSerializer):
#     user=CustomUserSerializer
#     items=OrderItemSerializer
#     shipping_address=StoreSerializer
#     class Meta:
#         model=Order
#         fields="__all__"


# class user_complainSerializer(serializers.ModelSerializer):
#     user=CustomUserSerializer
#     class Meta:
#         model=user_complain
#         fields="__all__"

# class UserOTPSerializer(serializers.ModelSerializer):
#     user=CustomUserSerializer
#     class Meta:
#         model = UserOTP


from django.contrib.auth.models import User
from requests import get
import geocoder
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import Group,Permission
from .serializers import *
from .views import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import viewsets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
class CustomUserViewSet(viewsets.ModelViewSet):#login
    queryset = CustomUser.objects.all() 
    serializer_class = CustomUserSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {'response_code':200,'comments':'All Roles',"status": True,'data': serializer.data}
        return Response(response_data)
    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    def create(self,request,*args,**kwargs):
        log_data=request.data
        try:
            user=CustomUser.objects.filter(username=log_data['username'])
            user_password=log_data['password']
        except:
            user=None
        if user:
            if user_password:
                if user[0].check_password(user_password):
                    serializer = self.get_serializer(user[0])
                    l=[serializer.data]
                    response_data = {'response_code':200,'comments':'User exists',"status": True,'data':l}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'Password is not matched',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'Your password is empty',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'Email not exists',"status": False}
            return Response(response_data)
    

class CustomUserSignupviewset(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    def list(self,request):
        query = CustomUser.objects.all()
        data= CustomUserSerializer(query)
        response_data = {'response_code':200,'comments':'get is not available for this url',"status": False}
        return Response(response_data)
    def create(self,request,*args,**kwargs):
        try:
            name=request.data['name']
            email=request.data['email']
            password=request.data['password']
            mobile=request.data['mobile']
        except:
            response_data = {'response_code':200,'comments':'All Fields is required',"status": False}
            return Response(response_data)
        if name=='' or email=='' or password=='' or mobile=='':
            response_data = {'response_code':200,'comments':'All Fields is required',"status": False}
            return Response(response_data)
        else:
            try:
                x=CustomUser(username=email,password=make_password(password),first_name=name,is_active=False)
                x.save()
            except:
                response_data = {'response_code':200,'comments':'Username is already taken',"status": False}
                return Response(response_data)
            try:
                newuser=UserProfile.objects.get(mobile=mobile)
                if newuser:
                    x.delete()
                    response_data = {'response_code':200,'comments':'This mobile number is already in use..',"status": False}
                    return Response(response_data)
            except:
                newuser=UserProfile(user=x,mobile=mobile)
                newuser.save()
                queryset = x
                serializer = self.get_serializer(queryset,context={'request': request})
                #serializer=UserProfileSerializer(newuser,context={'request': request})
                l=[serializer.data]
                usr_otp=random.randint(10000,99999)
                mobile_otp=random.randint(10000,99999)
                UserOTP.objects.create(user=x,otp=usr_otp,otp_mobile=mobile_otp)
                info=f"Hello {name},\n Your OTP is {usr_otp} \n Thanks!"
                '''try:
                    info=f"Hello {first_name},\n Your OTP is {usr_otp} \n Thanks!"
                    send_mail(
                        "Welcome to Momentostrust - Verify your email",
                        info,
                        settings.EMAIL_HOST_USER,   
                        [email],
                        fail_silently=False
                    )
                except:
                    x.delete()
                    response_data = {'response_code':200,'comments':'your email is is not valid',"status": False}
                    return Response(response_data)'''
                y=requests.get('http://sendsms.designhost.in/index.php/smsapi/httpapi/?uname=aaratechnologies&password=123456&sender=ATAARA&receiver={}&route=TA&msgtype=3&sms={}'.format(mobile,mobile_otp))
                user_inst=User.objects.get(username=email)
                tk=Token.objects.get(user=user_inst)
                response_data = {'response_code':200,'Token':tk.key,'comments':'OTP of mobile and email send to your respected mobile number, please validate it',"status": True,'data':l}
                return Response(response_data)


class OtpValidationViewset(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            email=request.data['email']
            mobile_otp=request.data['mobile_otp']
        except:
            mobile_otp=None
            email=None
        if mobile_otp  and email:
            try:
                user_obj=CustomUser.objects.get(username=email)
            except:
                user_obj=None
            if user_obj:
                user_otp=UserOTP.objects.filter(user=user_obj.id).last()
                if str(user_otp.otp_mobile)==str(mobile_otp):
                    user_obj.is_active=True
                    user_obj.save()
                    response_data = {'response_code':200,'comments':'OTP of mobile is varified..., You can login',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'Please enter current otp',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'User is not exists...',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'email and mobile otp are require...',"status": False}
            return Response(response_data)



class getmobileotpviewset(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            email=request.data['email']
        except:
            email=None
        if email:
            try:
                user_obj=CustomUser.objects.get(username=email)
            except:
                user_obj=None
        else:
            response_data = {'response_code':200,'comments':'Please enter your email... ',"status": False}
            return Response(response_data)

        if user_obj:
            try:
                userprofile_obj=UserProfile.objects.get(user=user_obj.id)
            except:
                userprofile_obj=None
            if userprofile_obj:
                reg_mobile=userprofile_obj.mobile
                send_mobile_otp(email,reg_mobile)
                response_data = {'response_code':200,'comments':'Otp has been send to your register  mobile number  ',"status": True}
                return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'your mobile number is not register...  ',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'this user is not exists..',"status": False}
            return Response(response_data)



class resetpasswordviewset(viewsets.ViewSet):
    def create(self,request,*args,**kwargs):
        try:
            email=request.data['email']
            mobile_otp=request.data['mobile_otp']
            password=request.data['password']
            confirm_password=request.data['confirm_password']
        except:
            response_data = {'response_code':200,'comments':'all fields is required..',"status": False}
        try:
            user_obj=CustomUser.objects.get(username=email)
        except:
            user_obj=None
        if user_obj:
            user_otp=UserOTP.objects.filter(user=user_obj.id).last()
            if mobile_otp==user_otp.otp_mobile:
                if password1==password2:
                    user_obj.password=make_password(password1)
                    user_obj.save()
                    response_data = {'response_code':200,'comments':'Your password has been changed.....',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'password and conform password should be same...',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'otp is not correct...',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'user email is not valid ...',"status": False}
            return Response(response_data)



# ##ac
# class Login_check(viewsets.ViewSet):
#     def create(self,request):
#         data=request.data
#         email1=data.get('email')
#         password1=data.get('password')
#         try:
#             user1=User.objects.get(username=email1)
#             if user1.check_password(password1):
#                 login(request,user1)
#                 response_data = {'response_code':200,'comments':'login is successful',"status": True}
#                 return Response(response_data)
#             else:
#                 response_data = {'response_code':200,'comments':'user is not authenticated',"status": False}
#                 return Response(response_data) 
#         except:
#             response_data = {'response_code':200,'comments':'user is not none',"status": False}
#             return Response(response_data) 
# ############################end login api ####################
# ############################start logout api ####################


class Logout_check(viewsets.ViewSet):
    def list(self,request):
        logout(request)
        response_data = {'response_code':200,'comments':'logout is successful',"status": True}
        return Response(response_data)    





class UserhomeapiViewset(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        productQuery=Product.objects.all()
        serializer=ProducttableSerializer(productQuery,many=True)
        response_data = {'response_code':200,'comments':'All Products',"status": True,'data': serializer.data}
        return Response(response_data)


class CategoryapiViewset(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        cat=Category.objects.all()
        serializer=CategorySerializer(cat,many=True)
        response_data = {'response_code':200,'comments':'All Category',"status": True,'data': serializer.data}
        return Response(response_data)


class SubCategoryapiViewset(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        sub_cat=SubCategory.objects.all()
        serializer=SubcategorySerializer(sub_cat,many=True)
        response_data = {'response_code':200,'comments':'All SubCategory',"status": True,'data': serializer.data}
        return Response(response_data)


from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *


# class MyAdminSite(AdminSite):
#     site_header = 'GK-Service'

# admin_site2 = MyAdminSite(name='myadmin_user')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserProfile._meta.fields]


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

class UserOTPAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserOTP._meta.fields]


class AddressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Address._meta.fields]

class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderItem._meta.fields]

class ComplainAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Complain._meta.fields]

class WishlistAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Wishlist._meta.fields]

class InvoiceDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InvoiceData._meta.fields]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(UserOTP,UserOTPAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Complain,ComplainAdmin)
admin.site.register(InvoiceData,InvoiceDataAdmin)

# admin_site2.register(Wishlist, WishlistAdmin)
# admin_site2.register(UserProfile)
# admin_site2.register(UserOTP,UserOTPAdmin)
# admin_site2.register(Address)
# admin_site2.register(OrderItem)
# admin_site2.register(Order)
# admin_site2.register(Complain)


#         fields = ('user','url','time_st','otp','otp_mobile')
