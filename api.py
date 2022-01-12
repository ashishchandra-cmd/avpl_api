from django.db import models

from django.contrib.auth.models import User,AbstractUser
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import mark_safe

# Create your models here.
############################################# User Registration #######################################################
class User_register(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    gender = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50,null=True)
    longitude = models.CharField(max_length=50,null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200,null=True)
    otp = models.CharField(max_length=20,null=True)
    profile_pic = models.ImageField(upload_to='profile_pic',null=True)
    utype = models.CharField(max_length=100,default='User')
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    update_date_time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username
    @property
    def profile_pic_preview(self):
        if self.profile_pic:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.profile_pic.url))
        return ""
    




# ########################################## Binary Tree ###############################################################3
# class TreeChain(MPTTModel):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     refer_by = models.CharField(max_length=100,default='ui')
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#     left = models.BooleanField()
#     right = models.BooleanField()

#     def __str__(self):
#         return self.user.username
#
# ########################################### Refer Code ###############################################################
class Refer_code(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    refercode = models.CharField(max_length=300)
    date_time  = models.DateTimeField(auto_now_add=True,null=True)
    update_date_time = models.CharField(max_length=100,null=True)
#
# ########################################## Category And Sub Ctaegory #################################################
#
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category',null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    update_date_time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='subcategory',null=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    update_date_time = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""
class Brands(models.Model):
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='brand',null=True)
    date_time  = models.DateTimeField(auto_now_add=True,null=True)
    update_date_time = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""

# ########################################################## PV Set Here ##################################################
#
class PVset(models.Model):
    Subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    PV = models.FloatField()
#
# ###################################################### Prouct Model Here ########################################################
class Vendor_registration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    store_mobile = models.IntegerField()
    vendor_status = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='vendor_profile_pic',null=True)
    store_status = models.BooleanField(default=False)
    store_remove = models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10,null=True)
    utype = models.CharField(max_length=100, default='Vendor')
    update_date_time = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username
    @property
    def profile_pic_preview(self):
        if self.profile_pic:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.profile_pic.url))
        return ""
    

class Vendor_Store_detail(models.Model):
    vendor = models.OneToOneField(Vendor_registration,on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    store_name = models.CharField(max_length=200)
    store_address = models.CharField(max_length=200,null=True)
    store_zipcode = models.CharField(max_length=20,null=True)
    store_latitude = models.CharField(max_length=200,null=True)
    store_longitude = models.CharField(max_length=200,null=True)
    store_description = models.TextField()
    store_registration_number = models.CharField(max_length=100,null=True)
    store_category = models.CharField(max_length=200)
    store_logo = models.ImageField(upload_to='store_logo')
    store_banner = models.ImageField(upload_to='store_banner')
    store_image = models.ImageField(upload_to='store_image')
    store_closing_day = models.CharField(max_length=200)
    store_closing_time = models.CharField(max_length=20)
    store_opening_time = models.CharField(max_length=20)
    store_created_at = models.DateTimeField(auto_now_add=True)
    store_update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    @property
    def store_logo_preview(self):
        if self.store_logo:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_logo.url))
        return ""
    @property
    def store_banner_preview(self):
        if self.store_banner:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_banner.url))
        return ""
    @property
    def store_image_preview(self):
        if self.store_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_image.url))
        return ""


class Vendor_store_document(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    store_seller_aadhar = models.IntegerField()
    store_seller_gst = models.CharField(max_length=100)
    store_seller_front_aadhar_image = models.FileField(upload_to='store_seller_aadhar_image')
    store_seller_back_aadhar_image = models.FileField(upload_to='store_seller_aadhar_image',null=True)
    store_seller_pancard = models.CharField(max_length=100)
    store_seller_pancard_image = models.FileField(upload_to='store_seller_pancard_image')
    store_shiping_policy = models.FileField(upload_to='shiping_policy',null=True)
    store_return_policy = models.FileField(upload_to='return_policy',null=True)
    store_bank_account_number = models.CharField(max_length=300)
    store_bank_name = models.CharField(max_length=100)
    store_bank_ifsc = models.CharField(max_length=100)
    store_bank_passbook = models.FileField(upload_to='store_bank_passbook')
    store_seller_razorpay_id = models.CharField(max_length=200,null=True)
    created = models.DateTimeField(auto_now_add=True)
    update_date_time = models.CharField(max_length=100,null=True)

    @property
    def store_seller_front_aadhar_image_preview(self):
        if self.store_seller_front_aadhar_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_seller_front_aadhar_image.url))
        return ""

    @property
    def store_seller_back_aadhar_image_preview(self):
        if self.store_seller_back_aadhar_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_seller_back_aadhar_image.url))
        return ""
    @property
    def store_seller_pancard_image_preview(self):
        if self.store_seller_back_aadhar_image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_seller_back_aadhar_image.url))
        return ""
    @property
    def store_shiping_policy_preview(self):
        if self.store_shiping_policy:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_shiping_policy.url))
        return ""
    
    @property
    def store_return_policy_preview(self):
        if self.store_return_policy:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_return_policy.url))
        return ""
    
    @property
    def store_bank_passbook_preview(self):
        if self.store_bank_passbook:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.store_bank_passbook.url))
        return ""

class Product(models.Model):
    VARIANTS = (
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stor_details=models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_percent = models.FloatField(blank=True, null=True)
    gst_percent = models.FloatField(blank=True, null=True)
    variant = models.CharField(max_length=10, choices=VARIANTS, default='Size')
    image = models.ImageField(upload_to='product', null=True)
    status = models.BooleanField(default=False)
    created_date =models.DateTimeField(auto_now_add=True,null=True)
    update_date = models.CharField(max_length=100,null=True)
    ecommerce_show_data = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def amount_to_pay(self):
        return self.price - self.price * (self.discount_percent / 100)

    def amount_to_pay_retailer(self):
        return self.retailer_price - self.price * (self.discount_percent / 100)

    # def image_tag(self):
    #     if self.image.url is not None:
    #         return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #     else:
    #         return ""
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.URLField(max_length=6000, blank=True)

    def __str__(self):
        return self.title
    # @property
    # def image_preview(self):
    #     if self.image:
    #         return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
    #     return ""


# class Comment(models.Model):
#     STATUS = (
#         ('New', 'New'),
#         ('True', 'True'),
#         ('False', 'False'),
#     )
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=50, blank=True)
#     comment = models.CharField(max_length=250, blank=True)
#     rate = models.IntegerField(default=1)
#     status = models.CharField(max_length=10, choices=STATUS, default='New')
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.subject


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""


class Size(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10, blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name


class Variants(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True)
    image_fornt = models.ImageField(upload_to='image_front',null=True)
    image_back = models.ImageField(upload_to='image_back',null=True)
    image_side = models.ImageField(upload_to='image_side',null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    weight = models.FloatField(null=True)
    point_value = models.FloatField(null=True)
    after_discount_price = models.FloatField(null=True)
    variant_discount = models.FloatField(null=True)
    variant_show_status = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    update_date_time = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.title

    # def image(self):
    #     img = Images.objects.get(id=self.image_id)
    #     if img.id is not None:
    #         varimage = img.image.url
    #     else:
    #         varimage = ""
    #     return varimage

    # def image_tag(self):
    #     img = Images.objects.get(id=self.image_id)
    #     if img.id is not None:
    #         return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
    #     else:
    #         return ""
    @property
    def image_fornt_preview(self):
        if self.image_fornt:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image_fornt.url))
        return ""
    @property
    def image_back_preview(self):
        if self.image_back:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image_back.url))
        return ""
    
    @property
    def image_side_preview(self):
        if self.image_side:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image_side.url))
        return ""







# ######################################################Product Buy For adding Tree ###################################################
# class buy_sponser(models.Model):
#     product_name = models.CharField(max_length=50)
#     username = models.CharField(max_length=150)
#     price = models.FloatField()
#     image =models.ImageField(upload_to='images')
#
# ###################################################Product Buy add Tree and adress form models ##########################################
#
# class Sponser_user_address(models.Model):
#     username = models.CharField(max_length=100)
#     name=models.CharField(max_length=100,default='a')
#     sponserid = models.CharField(max_length=100)
#     position= models.CharField(max_length=100)
#     address = models.TextField()
#     address2 = models.TextField()
#     city = models.CharField(max_length=200)
#     zipcode = models.IntegerField()
#     amount= models.FloatField()
#     payment_id = models.CharField(max_length=100,default="no")
#     signature = models.CharField(max_length=200,default='no')
#     product_name = models.CharField(max_length=200,default='no')
#     order_id = models.CharField(max_length=100,default='no')
#     Paid=models.BooleanField(default=False)
#     #datetime = models.DateTimeField(auto_now_add=True,null=True,default=datetime.now)
# #####################################################Direct refer Statement genrate here############################################
#
# class Direct_refer_statements(models.Model):
#     username=models.CharField(max_length=100)
#     desc = models.CharField(max_length=100)
#     amount = models.FloatField()
#     date_time = models.DateTimeField(auto_now_add=True)
#
# ################################################ Cart ###############################################################
#
class UserCart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    variant_id = models.ForeignKey(Variants,on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField()
    store_user = models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    final_price = models.FloatField(default='0.0')
    cart_status = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    update_date_time = models.CharField(max_length=100,null=True)

############################################# Contact Form #######################################

class contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.IntegerField()
    message = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
############################################# For Otp matching #####################################3
class Otp(models.Model):
    email=models.CharField(max_length=100)
    otp=models.CharField(max_length=20)

########################################### Wishlist ################################################

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    store_user = models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    variant_id = models.OneToOneField(Variants,on_delete=models.CASCADE)
    date_time =models.DateTimeField(auto_now_add=True,null=True)
####################################  Randm address picker by user ################################

class random_address(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True,null=True)

################################ baneer model ##############################

class Banner(models.Model):
    image = models.ImageField(upload_to='banner')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""


############################ Product Shipping Address #################

class Delivery_address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.PositiveIntegerField()
    locality = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200,null=True)
    alternate_mobile = models.IntegerField(null=True)
    order_mode = models.CharField(max_length=100,null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)

#########################################################################################################################################
###################### Fake product table only use for order######################

class Product_fake(models.Model):
    Buyer = models.ForeignKey(User,on_delete=models.CASCADE)
    stor_details=models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_percent = models.FloatField(blank=True, null=True)
    gst_percent = models.FloatField(blank=True, null=True)
    variant = models.CharField(max_length=10)
    image = models.ImageField(upload_to='product_fake', null=True)
    created_date =models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    def amount_to_pay(self):
        return self.price - self.price * (self.discount_percent / 100)

    def amount_to_pay_retailer(self):
        return self.retailer_price - self.price * (self.discount_percent / 100)

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

###################### end fake product table/only user for order ########################

######################## fake variant table ##################


class Variants_fake(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    product = models.ForeignKey(Product_fake, on_delete=models.CASCADE)
    real_var_id = models.IntegerField(null=True)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    description = models.TextField(null=True)
    image_fornt = models.ImageField(upload_to='image_front_fake',null=True)
    image_back = models.ImageField(upload_to='image_back_fake',null=True)
    image_side = models.ImageField(upload_to='image_side_fake',null=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    point_value = models.FloatField(null=True)
    after_discount_price = models.FloatField(null=True)
    variant_discount = models.FloatField(null=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.title

    def image(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            varimage = img.image.url
        else:
            varimage = ""
        return varimage

    def image_tag(self):
        img = Images.objects.get(id=self.image_id)
        if img.id is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(img.image.url))
        else:
            return ""


#################### order detail / History ###################################
class Order_detail(models.Model):
    order_stat = (
        ('Deliver', 'Deliver'),
        ('Booked', 'Booked'),
        ('Cancel', 'Cancel'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ManyToManyField(Variants_fake)
    store_user = models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    payment_mode = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=200)
    order_id = models.CharField(max_length=200)
    signature=models.CharField(max_length=200)
    order_status = models.CharField(default='Booked',choices=order_stat,max_length=100)
    delivery_status = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    cancel_date = models.CharField(max_length=50,null=True)
    delivery_address = models.ForeignKey(Delivery_address,on_delete=models.CASCADE,null=True)
    time_slot = models.CharField(max_length=100,null=True)
    order_mode = models.CharField(max_length=40)
    price = models.FloatField()
    oreder_cancel_reason = models.TextField(null=True)

#############################End  Product Shipping Address #################
################################################################
#################### order detail / History ###################################
# class Order_detail(models.Model):
#     order_stat = (
#         ('Deliver', 'Deliver'),
#         ('Booked', 'Booked'),
#         ('Cancel', 'Cancel'),
#     )
#     order = (
#         ('Self_Picking','Self_Pickig'),
#         ('Delivery','Delivery'),
#     )
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     item = models.ManyToManyField(UserCart)
#     store_user = models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
#     payment_mode = models.CharField(max_length=100)
#     payment_id = models.CharField(max_length=200)
#     order_id = models.CharField(max_length=200)
#     signature=models.CharField(max_length=200)
#     order_status = models.CharField(default='Booked',choices=order_stat,max_length=100)
#     delivery_status = models.BooleanField(default=False)
#     date_time = models.DateTimeField(auto_now_add=True)
#     cancel_date = models.CharField(max_length=50,null=True)
#     delivery_address = models.ForeignKey(Delivery_address,on_delete=models.CASCADE,default=1)
#     time_slot = models.CharField(max_length=100,null=True)
#     order_mode = models.CharField(max_length=40,choices=order,default='Order')
#     price = models.FloatField()
#     question = models.CharField(max_length=200,null=True)
#     answer = models.TextField(null=True)

#############################End  Product Shipping Address #################
class vendor_time_slot(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vendor_store = models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    from_time = models.CharField(max_length=100)
    to_time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

################ Bottom Banner ##############################


class Bottom_Banner(models.Model):
    image = models.ImageField(upload_to='bottom_banner')
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
        return ""


################# End Bottom banner ##########################


################refer_id_store/position#########################

class Refer_id_store(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    refer_code = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True,null=True)


##################enn refere_id_sotre/position#################

class LikesModelVariant(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    variants=models.ForeignKey(Variants,on_delete=models.CASCADE)
    comments=models.CharField(max_length=300)
    likes=models.CharField(max_length=100)
    rating=models.FloatField()

class LikesModelShop(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shop=models.ForeignKey(Vendor_Store_detail,on_delete=models.CASCADE)
    comments=models.CharField(max_length=300)
    rating=models.FloatField()



class AvgRating(models.Model):
    product=models.ForeignKey(Variants,on_delete=models.CASCADE)
    avg_rating=models.FloatField()
    count_rating=models.CharField(max_length=100)





#serilizerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','username','first_name','last_name']
class UserRegisterSerializers(serializers.ModelSerializer):
    # user=UserSerializers()
    class Meta:
        model=User_register
        # fields = ['user','mobile','gender','address']
        fields='__all__'



class VendorRegisterSerializers(serializers.ModelSerializer):
        user=UserSerializers()
        class Meta:
            model=Vendor_registration
            # fields = ['user','store_mobile','gender','store_address']
            fields='__all__'
class VendorStoreDetailSerializers(serializers.ModelSerializer):
    # user=UserSerializers()
    class Meta:
        model=Vendor_Store_detail()
        fields='__all__'


class VendorRegStodcuDetSerializers(serializers.ModelSerializer):
    user=UserSerializers()
    class Meta:
        model=Vendor_store_document()
        # fields=['user','store_seller_aadhar','store_seller_gst','store_seller_front_aadhar_image','store_seller_back_aadhar_image',
        #         'store_seller_pancard','store_seller_pancard_image','store_shiping_policy',
        #           'store_return_policy','store_bank_account_number','store_bank_name','store_bank_ifsc',
        #            'store_bank_passbook','store_seller_razorpay_id','created']
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        # fields=['name','email','mobile','message','datetime']
        fields='__all__'
############################################################ filter######
##all in one me views and url bana padega
class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model=Product
        # fields=['title','description','retailer_price','price','gst_percent','discount_percent','quantity']
        fields='__all__'

class SubSubcategorySerializer(serializers.ModelSerializer):
    # subcategory=SubcategorySerializer()
    product=ProductSerialize(many=True)
    class Meta:
        model=Brands
        fields=['name','product']#'subcategory',


class SubcategorySerializer(serializers.ModelSerializer):
    # category=CategorySerializer()
    subsubcategory=SubSubcategorySerializer(many=True)
    class Meta:
        model=Subcategory
        fields=['name','subsubcategory']#'category',
#reverse me jaye ga data,CategorySerializer se all list ayega
class CategorySerializer(serializers.ModelSerializer): 
    subcategory=SubcategorySerializer(many=True)
    class Meta:
        model=Category
        fields=['name','subcategory']


# https://www.youtube.com/watch?v=EyMFf9O6E60
######### only catgery list#########

class CategorySerializer_only(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        # fields=['id','name','image']
        fields='__all__'

class SubcategorySerializer_only(serializers.ModelSerializer):
    class Meta:
        model=Subcategory
        fields=['category_id','id','name','image']
class SubSubcategorySerializer_only(serializers.ModelSerializer):
    
    class Meta:
        model=Brands
        fields=['subcategory_id','id','name','image']
        # fields='__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        # fields=['id','image','title','description']
        fields='__all__'
        

class Bottom_BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bottom_Banner
        # fields=['id','image','title','description']
        fields='__all__'



class ProductSerializeALL(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields='__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields='__all__'

============================================================================================================

from django.urls import path
from app import api_views
urlpatterns = [
    path('user_list/',api_views.UserRegister.as_view({'get':'list'})),
    path('user_register/',api_views.UserRegister.as_view({'post':'create'})),
    path('user_register_delete/<int:id>/',api_views.UserRegister.as_view({'delete':'destroy'})),
    path('user_resend_mail_otp/',api_views.UserResendMailOtp.as_view({'post':'create'})),
    path('user_otp_verify/',api_views.UserOtpVerify.as_view({'post':'create'})),
    path('user_change_pwd/',api_views.UserChangePwd.as_view({'post':'create'})),
    path('user_update/<int:id>/',api_views.UserRegister.as_view({'put':'update'})),


    path('contact_create/',api_views.Contactall.as_view({'post':'create'})),
    path('contact_list/',api_views.Contactall.as_view({'get':'list'})),
    path('contact_delete/<int:id>/',api_views.Contactall.as_view({'delete':'destory'})),

    path('vendor_register/',api_views.VendorRegister.as_view({'post':'create'})),
    path('vendor_list/',api_views.VendorRegister.as_view({'get':'list'})),
    path('vendor_resend_mail_Otp/',api_views.VendorResendMailOtp.as_view({'post':'create'})),
    path('vendor_otp_verify/',api_views.VendorOtpVerify.as_view({'post':'create'})),
    path('vendor_change_pwd/',api_views.VendorChangePwd.as_view({'post':'create'})),
    path('vendor_update/<int:id>/',api_views.VendorRegister.as_view({'put':'update'})),
    path('vendor_register_store_details/',api_views.VendorRegisterStoreDetails.as_view({'post':'create'})),
    path('vendor_register_store_details_list/',api_views.VendorRegisterStoreDetails.as_view({'get':'list'})),
    path('vendor_store_update/<int:id>/',api_views.VendorRegisterStoreDetails.as_view({'put':'update'})),
    path('vendor_register_store_dcument_detail/',api_views.VendorRegisterStoredcumentDetail.as_view({'post':'create'})),
    path('vendor_register_store_dcument_detail_list/',api_views.VendorRegisterStoredcumentDetail.as_view({'get':'list'})),

    path('category_list/',api_views.CategoryALL.as_view({'get':'list'})),
    path('category_create/',api_views.CategoryALL.as_view({'post':'create'})),
    path('category_update/<int:id>/',api_views.CategoryALL.as_view({'put':'update'})),
    path('category_delete/<int:id>/',api_views.CategoryALL.as_view({'delete':'destory'})),

    path('subcategory_list/',api_views.SubcategoryALL.as_view({'get':'list'})),
    path('subcategory_list_by-category/',api_views.SubcategoryALL.as_view({'post':'create'})),

    path('brands_list/',api_views.SubSubcategoryAll.as_view({'get':'list'})),
    path('brands_list_by_subcategory/',api_views.SubSubcategoryAll.as_view({'post':'create'})),


    path('login/',api_views.Login_check.as_view({'post':'create'})),
    path('logout/',api_views.Logout_check.as_view({'get':'list'})),

    path('banner_list/',api_views.BannerALL.as_view({'get':'list'})),
    path('forget_password/',api_views.Forget_password.as_view({'post':'create'})),
    path('forget_password_verify_otp/',api_views.Forget_Password_Verify_Otp.as_view({'post':'create'})),
    path('forget_password_resend_otp/',api_views.Forget_Password_Resend_Otp.as_view({'post':'create'})),
    path('product_list/',api_views.ProductALL.as_view({'get':'list'})),
    path('product_list_by_stor/',api_views.ProductALL.as_view({'post':'create'})),
    path('image_list/',api_views.ImageAll.as_view({'get':'list'})),
    path('color_size_brand_list/',api_views.ColorSizeBrandAll.as_view({'get':'list'})),
    path('Variants_brand_color_size_list/',api_views.VariantsAll.as_view({'post':'create'})),
    path('addres_search_for_shop/',api_views.Addres_Search_For_Shop.as_view({'post':'create'})),
    path('addres_search_for_shop_after_login/',api_views.Addres_Search_For_Shop_after_Login.as_view({'post':'create'})),
    path('bottom_banner_list/',api_views.Bottom_BannerAll.as_view({'get':'list'})),
    path('variant_subcategry_stor_list/',api_views.VariantbySubcategryStor.as_view({'post':'create'})),
    path('variantby_ubcategry_list/',api_views.VariantbySubcategry.as_view({'post':'create'})),
    path('variantby_subcategry_list/',api_views.VariantbySubcategry.as_view({'post':'create'})),


    path('user_cart_varint_add/',api_views.UserCartAdd.as_view({'post':'create'})),
    path('cart_show/',api_views.CartShow.as_view({'post':'create'})),
    path('cart_remove/',api_views.CartRemove.as_view({'post':'create'})),
    path('cart_plus/',api_views.CartPlus.as_view({'post':'create'})),
    path('cart_minus/',api_views.CartMinus.as_view({'post':'create'})),

    path('wishlist/',api_views.WishlistList.as_view({'post':'create'})),
    path('wishlist_by_user/',api_views.WishlistByUser.as_view({'post':'create'})),
    path('wishlist_remove/',api_views.WishlistRemove.as_view({'post':'create'})),
    path('delivery_address_create/',api_views.DeliveryAddressCreate.as_view({'post':'create'})),
    path('delivery_address_update/',api_views.DeliveryAddressUpdate.as_view({'post':'create'})),
    path('delivery_address_delete/',api_views.DeliveryAddressDelete.as_view({'post':'create'})),
    
    # path('checkout_create/',api_views.CheckOut.as_view({'post':'create'})),
    # path('time_slot_payment/',api_views.TimeslotPayment.as_view({'post':'create'})),
    # path('succcess_payment_razorpay/',api_views.SucccessPaymentRazorpay.as_view({'post':'create'})),
    # path('payment_by_cod/',api_views.PaymentByCod.as_view({'post':'create'})),
    path('order_detail_by_user/',api_views.OrderDetailByUser.as_view({'post':'create'})),
    path('order_cancel/',api_views.OrderCancel.as_view({'post':'create'})),

    path('delivery_address_list_by_user/',api_views.DeliveryAddressListByUser.as_view({'post':'create'})),

    path('show_rating_details_varint/',api_views.ShowRatingDetailsVariant.as_view({'post':'create'})),
    path('create_rating_details_varint/',api_views.CreateRatingDetailsVariant.as_view({'post':'create'})),
    path('delete_rating_detail_varint/',api_views.DeleteRatingDetailVarint.as_view({'post':'create'})),

    path('show_rating_detail_shop/',api_views.ShowRatingDetailShop.as_view({'post':'create'})),
    path('create_rating_detail_shop/',api_views.CreateRatingDetailShop.as_view({'post':'create'})),
    path('delete_rating_detail_shop/',api_views.DeleteRatingDetailShop.as_view({'post':'create'})),
    
    path('refer_id_store_create/',api_views.ReferIdStoreCreate.as_view({'post':'create'})),
    path('refer_id_store_update/',api_views.ReferIdStoreUpdate.as_view({'post':'create'})),
    path('refer_id_store_list/',api_views.ReferIdStoreList.as_view({'get':'list'})),
    path('refer_id_store_list_byuser/',api_views.ReferIdStoreListByUser.as_view({'post':'create'})),

    path('refer_code_create/',api_views.ReferCodeCreate.as_view({'post':'create'})),
    path('refer_code_list/',api_views.ReferCodeList.as_view({'get':'list'})),
    path('refer_code_list_by_user/',api_views.ReferCodeListByUser.as_view({'post':'create'})),
    #################
    path('random_address_create/',api_views.RandomAddress.as_view({'post':'create'})),
    path('nandom_address_update/',api_views.RandomAddressUpdate.as_view({'post':'create'})),
    path('random_address_delete/',api_views.RandomAddressDelete.as_view({'post':'create'})),
    path('selfpicking_Mode/',api_views.SelfPickingMode.as_view({'post':'create'})),
    path('succcess_payment_razorpay_new/',api_views.SucccessPaymentRazorpayNew.as_view({'post':'create'})),
    path('payment_by_cod/',api_views.PaymentByCod.as_view({'post':'create'})),
]




======================================



from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
import re
from random import randint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import geocoder
import googlemaps
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from rest_framework import status
from avpl.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import razorpay
import datetime
from django.db.models import Avg , Count



class UserRegister(ViewSet):
    def list(self,request):
        query=User_register.objects.all()
        seriler=UserRegisterSerializers(query,many=True)
        users={'User_register':seriler.data,'response_code':200,'comments':'all list',"status": True}
        return Response(users)

    def create(self,request):
        data=request.data
        ###session set####
        request.session['first_name']=data.get('first_name')
        request.session['last_name']=data.get('last_name')
        request.session['password']=data.get('password')
        request.session['email']=data.get('email')
        request.session['mobile']=data.get('mobile')
        request.session['gender']=data.get('gender')
        request.session['address']=data.get('address')
        ####session get#####
        email1 = request.session.get('email')
        password1 = request.session.get('password')
        try:
            user_object=User.objects.get(username=email1)#instance username me email save ho rha
            response_data = {'response_code':200,'email':email1,'comments':'email is allredy exist',"status": False}
            return Response(response_data)
        except:
            rand_otp = randint(1111, 9999)
            try:
                otp_check=Otp.objects.get(email=email1)
                otp_check.email=email1
                otp_check.otp=rand_otp
                otp_check.save()
            except:
                otp_obj=Otp(otp=rand_otp,email=email1)
                otp_obj.save()
        
            send_conformation_email(request,rand_otp)
            response_data = {'response_code':200,'email':email1,'comments':'otp is send please veryfy',"status": True}
            return Response(response_data)
        
    
    def destroy(self,request,id=None):
        try:
            ts=User_register.objects.get(id=id)
            ts.delete()
            response_data = {'response_code':200,'comments':'User_register is succeefull deleted',"status": True}
            return Response(response_data)
        except User_register.DoesNotExist:
            response_data = {'response_code':200,'comments':'User_register is invalid',"status": False}
            return Response(response_data)
    def update(self,request,id=None):
        data=request.data
        email1=data.get('email')
        first_name1=data.get('first_name')
        last_name1=data.get('last_name')
        mobile1=data.get('mobile')
        address1=data.get('address')
        try:
            user_inst = User.objects.get(username=email1)#instance
            print(user_inst)
            obj = User_register.objects.get(user=user_inst)
            print(obj)
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            add_lat_long = gmaps.geocode(address1)
            user_lat = add_lat_long[0]['geometry']['location']['lat']
            user_lng = add_lat_long[0]['geometry']['location']['lng']
            obj.address=address1
            obj.latitude = user_lat
            obj.longitude = user_lng
            obj.mobile = mobile1
            obj.save()
            obb = User.objects.get(username=email1)
            obb.first_name =first_name1
            obb.last_name =last_name1
            obb.save()
            response_data = {'response_code':200,'comments':'user is succeefull update',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'user not  register',"status": False}
            return Response(response_data)


class UserResendMailOtp(ViewSet):
    def create(self,request):
        email = request.data.get('email') 
        print(email)
        rand_otp = randint(1111, 9999)
        otp_update = Otp.objects.get(email=email)
        otp_update.otp=rand_otp
        print('otp_update',otp_update)
        otp_update.save()
        send_conformation_email(request,rand_otp)
        response_data = {'response_code':200,'comments':'Resend OTP Successfully on your register Email..Please Verify Email',"status": True}
        return Response(response_data)
class UserOtpVerify(ViewSet):
    def create(self,request):
        # data=request.data
        first_name1 = request.data.get('first_name')
        last_name1 = request.data.get('last_name')
        password1 = request.data.get('password')
        gender1 = request.data.get('gender')
        mobile1 = request.data.get('mobile')
        email1=request.data.get('email')
        address1 = request.data.get('address')
        otp_check=Otp.objects.get(email=email1)
        print(otp_check)
        print("yes run here..")
        otpByuser=request.data.get('otp')#ye postman me fildname rahega ,jsme gmail wala otp rega
        print(otpByuser)
        if otp_check.otp==str(otpByuser):
            usr_obj=User(username=email1,first_name=first_name1,last_name=last_name1,password=make_password(password1))
            usr_obj.save()
            user_inst=User.objects.get(username=email1)
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            add_lat_long = gmaps.geocode(address1)
            user_lat = add_lat_long[0]['geometry']['location']['lat']
            user_lng = add_lat_long[0]['geometry']['location']['lng']
            rest_obj=User_register(user=user_inst,mobile=mobile1,gender=gender1,address=address1,latitude=user_lat,longitude=user_lng)
            rest_obj.save()
            otp_check.delete()
            response_data = {'response_code':200,'comments':'register is successful',"status": True}
            return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'give valid otp',"status": False}
            return Response(response_data)

class UserChangePwd(ViewSet):
    def create(self,request):
        datas=request.data
        email1=datas.get('email')
        current_pwd=datas.get('current_password')
        new_pwd=datas.get('new_password')
        confirm_pwd=datas.get('confirm_password')
        # print(email1,current_pwd,new_pwd,confirm_pwd)
        user=authenticate(username=email1,password=current_pwd)
        print(user)
        if user is not None:
            print('111',user)
            if new_pwd==confirm_pwd:
                pwd_re = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                match_pwd = re.compile(pwd_re)
                res = re.search(match_pwd, new_pwd)
                if res:
                    user_inst=User.objects.get(username=email1)#update pwd
                    user_inst.password=make_password(new_pwd)
                    user_inst.save()
                else:
                    response_data = {'response_code':200,'comments':'password most be strong',"status":False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'password not matched',"status":False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'user is not valide',"status":False}
            return Response(response_data)


        response_data = {'response_code':200,'comments':'Password Chnange Successfully',"status":True}
        return Response(response_data)




############################ start vendor register api ####################

class VendorRegister(ViewSet):
    def list(self,request):
        query=Vendor_registration.objects.all()
        seriler=VendorRegisterSerializers(query,many=True)
        vrdr={'Vendor_registration':seriler.data,'response_code':200,'comments':'all list',"status": True}
        return Response(vrdr)
    def create(self,request):
        data=request.data
        ###session set####
        request.session['first_name']=data.get('first_name')
        request.session['last_name']=data.get('last_name')
        request.session['password']=data.get('password')
        request.session['repassword']=data.get('repassword')
        request.session['email']=data.get('email')
        request.session['mobile']=data.get('mobile')
        request.session['gender']=data.get('gender')
        request.session['address']=data.get('address')
        request.session['zipcode']=data.get('zipcode')
        ####session get#####
        email1 = request.session.get('email')
        password1 = request.session.get('password')
        password2 = request.session.get('repassword')
        # print(email1,password1,password2)
        # return Response('ok')
        try:
            user_object=User.objects.get(username=email1)#instance username me email save ho rha
            return Response('email is allredy exist')
        except:
            if password1==password2:
                pwd_reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                pwd_match_reg = re.compile(pwd_reg)
                # searching regex
                pwd = re.search(pwd_match_reg, password1)
                if pwd:
                    rand_otp = randint(1111, 9999)
                    try:
                        otp_check=Otp.objects.get(email=email1)
                        otp_check.email=email1
                        otp_check.otp=rand_otp
                        otp_check.save()
                    except:
                        otp_obj=Otp(otp=rand_otp,email=email1)
                        otp_obj.save()
                    #######
                    fromaddr='masterpython64@gmail.com'
                    toaddr=email1
                    msg=MIMEMultipart()
                    msg['From']=fromaddr
                    msg['To']=toaddr
                    msg['Subject']="otp for register"
                    body="Your OTP is,"+str(rand_otp)
                    msg.attach(MIMEText(body, 'plain'))
                    s = smtplib.SMTP('smtp.gmail.com', 587)
                    # start TLS for security
                    s.starttls()
                    # Authentication
                    s.login(fromaddr, "ashish@#2021")
                    # Converts the Multipart msg into a string
                    text = msg.as_string()
                    # sending the mail
                    s.sendmail(fromaddr, toaddr, text)
                    # terminating the session
                    s.quit()
                    response_data = {'response_code':200,'comments':'otp is send please veryfy',"status":True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'password invalid',"status":False}
                    return Response(response_data)                
            else:
                response_data = {'response_code':200,'comments':'password not match',"status":False}
                return Response(response_data)
    def update(self,request,id=None):
        data=request.data
        email1=data.get('email')
        first_name1=data.get('first_name')
        last_name1=data.get('last_name')
        mobile1=data.get('mobile')
        address1=data.get('address')
        try:
            user_inst = User.objects.get(username=email1)#instance
            print(user_inst)
            obj = Vendor_registration.objects.get(user=user_inst)
            print(obj)
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            add_lat_long = gmaps.geocode(address1)
            user_lat = add_lat_long[0]['geometry']['location']['lat']
            user_lng = add_lat_long[0]['geometry']['location']['lng']
            obj.store_address=address1
            obj.store_latitude = user_lat
            obj.store_longitude = user_lng
            obj.store_mobile = mobile1
            obj.save()
            obb = User.objects.get(username=email1)
            obb.first_name =first_name1
            obb.last_name =last_name1
            obb.save()
            response_data = {'response_code':200,'comments':'user is succeefull update',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'user not  register',"status": False}
            return Response(response_data)

############################ end vendor register api ####################
class VendorResendMailOtp(ViewSet):
    def create(self,request):
        email = request.session.get('email')
        print(email)
        otp = randint(1111, 9999)
        print(ot)
        otp_update = Otp.objects.get(email=email)
        otp_update.otp=otp
        print(otp_update)
        otp_update.save()
        fromaddr = 'masterpython64@gmail.com'
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Testing For Otp"
        body = "Your OTP is," + str(otp)
        msg.attach(MIMEText(body, 'plain'))
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # start TLS for security
        s.starttls()
        # Authentication
        s.login(fromaddr, "ashish@#2021")
        # Converts the Multipart msg into a string
        text = msg.as_string()
        # sending the mail
        s.sendmail(fromaddr, toaddr, text)
        # terminating the session
        s.quit()
        return Response('Resend OTP Successfully on your register Email..Please Verify Email')
############################ start VendorOtpVerify api ####################
class VendorOtpVerify(ViewSet):
    def create(self,request):
        data=request.data
        first_name1 = request.session.get('first_name')
        last_name1 = request.session.get('last_name')
        password1 = request.session.get('password')
        gender1 = request.session.get('gender')
        mobile1 = request.session.get('mobile')
        email1=request.session.get('email')
        address1 = request.session.get('address')
        zipcode1=request.session.get('zipcode')
        otp_check=Otp.objects.get(email=email1)
        print(otp_check)
        print("yes run here..")
        otpByuser=data.get('otp')#ye postman me fildname rahega ,jsme gmail wala otp rega
        print(otpByuser)
        if otp_check.otp==str(otpByuser):
            usr_obj=User(username=email1,first_name=first_name1,last_name=last_name1,password=make_password(password1))
            usr_obj.save()
            user_inst=User.objects.get(username=email1)
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            if address1:
                add_lat_long = gmaps.geocode(address1)
                vendor_lat = add_lat_long[0]['geometry']['location']['lat']
                vendor_lng = add_lat_long[0]['geometry']['location']['lng']
                rest_obj=Vendor_registration(user=user_inst, store_mobile=mobile1,profile_pic='tree_user_img.jpg', gender=gender1, store_address=address1,store_zipcode=zipcode1,store_latitude=vendor_lat,store_longitude=vendor_lng)
                rest_obj.save()
                otp_check.delete()
                response_data = {'response_code':200,'comments':'register is successful',"status": True}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'give valid otp',"status": False}
            return Response(response_data)

class VendorChangePwd(ViewSet):
    def create(self,request):
        datas=request.data
        email1=datas.get('email')
        current_pwd=datas.get('current_password')
        new_pwd=datas.get('new_password')
        confirm_pwd=datas.get('confirm_password')
        # print(email1,current_pwd,new_pwd,confirm_pwd)
        user=authenticate(username=email1,password=current_pwd)
        print(user)
        if user is not None:
            print('111',user)
            if new_pwd==confirm_pwd:
                pwd_re = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                match_pwd = re.compile(pwd_re)
                res = re.search(match_pwd, new_pwd)
                if res:
                    user_inst=User.objects.get(username=email1)#update pwd
                    user_inst.password=make_password(new_pwd)
                    user_inst.save()
                else:
                    return Response({'message':'password most be strong'})
            else:
                return Response({'message':'password not matched'})
        else:
            return Response({'message':'user is not valide'})

        return Response({'message':'Password Chnange Successfully'})


class VendorRegisterStoreDetails(ViewSet):
    def list(self,request):
        query=Vendor_Store_detail.objects.all()
        vendr=Vendor_registration.objects.all()
        if query:

            dat_dict={}
            data_list=[]

            for x in query:
                dat_dict={'user_id':x.vendor.user.id,'username':x.vendor.user.username,'first_name':x.vendor.user.first_name,'last_name':x.vendor.user.last_name,
                'store_mobile':x.vendor.store_mobile,'vendor_status':x.vendor.vendor_status,'profile_pic':str(x.vendor.profile_pic),
                'store_status':x.vendor.store_status,'store_remove':x.vendor.store_remove,'created':x.vendor.created,
                'gender':x.vendor.gender,'utype':x.vendor.utype,
                'store_id':x.id,'store_name':x.store_name,
                'store_address':x.store_address,'store_zipcode':x.store_zipcode,'store_latitude':x.store_latitude,
                'store_longitude':x.store_longitude,'store_category':x.store_category,'store_description':x.store_description,'store_registration_number':x.store_registration_number,
                'store_image':str(x.store_image),'store_logo':str(x.store_logo),'store_banner':str(x.store_banner),
                'store_closing_day':x.store_closing_day,'store_closing_time':x.store_closing_time,'store_opening_time':x.store_opening_time
                ,'store_created_at':x.store_created_at,'store_update_at':x.store_update_at}
                data_list.append(dat_dict)
            shop_dict={"Vendor_shop_details":data_list,'response_code':200,'comments':'all list',"status": True}
           
            return Response(shop_dict)
        else:
            shop_dict={'response_code':200,'comments':'no details of shop',"status": False}
            return Response(shop_dict)


    def create(self,request):
        datas=request.data
        email=datas.get('email')
        store_name = datas.get('store_name')
        store_description = datas.get('store_description')
        store_logo = datas.get('store_logo')
        store_banner = datas.get('store_banner')
        store_image = datas.get('store_image')
        store_category = datas.get('category')
        store_opening_time =datas.get('store_open_time')
        store_close_time =datas.get('store_close_time')
        store_cloasing_day =datas.get('store_day')
        store_registration_number =datas.get('store_registration_number')
        print('11111')
        try:
            user_instance = User.objects.get(username=email)
            store_detail = Vendor_Store_detail(user=user_instance,store_registration_number=store_registration_number,store_name=store_name,store_description=store_description,store_category=store_category,store_logo=store_logo,store_banner=store_banner,store_image=store_image,store_closing_day=store_cloasing_day,store_closing_time=store_close_time,store_opening_time=store_opening_time)
            store_detail.save()
            response_data = {'response_code':status.HTTP_201_CREATED,'comments':'Store Details successful register',"status": True}
            return Response(response_data)
        except:

            response_data = {'response_code':status.HTTP_404_NOT_FOUND,'comments':'venodor is not register',"status": False}
            return Response(response_data)
    def update(self,request,id=None):
        datas=request.data
        email=datas.get('email')
        store_name1 = datas.get('store_name')
        store_description1 = datas.get('store_description')
        store_logo1 = datas.get('store_logo')
        store_banner1 = datas.get('store_banner')
        store_image1 = datas.get('store_image')
        store_opening_time1 =datas.get('store_open_time')
        store_close_time1 =datas.get('store_close_time')
        store_cloasing_day1 =datas.get('store_day')
        try:
            user_inst = User.objects.get(username=email1)#instance
            print(user_inst)
            obj = Vendor_Store_detail.objects.get(user=user_inst)
            print(obj)
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            add_lat_long = gmaps.geocode(address1)
            user_lat = add_lat_long[0]['geometry']['location']['lat']
            user_lng = add_lat_long[0]['geometry']['location']['lng']
            obj.store_name=store_name1
            obj.store_description=store_description1
            obj.store_logo = store_logo1
            obj.store_banner = store_banner1
            obj.store_image = store_image1
            obj.store_closing_day=store_cloasing_day1
            obj.store_closing_time=store_close_time1
            obj.store_opening_time=store_opening_time1
            obj.save()
            
            response_data = {'response_code':200,'comments':'Store Details successful update',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'Store not  register',"status": False}
            return Response(response_data)




class VendorRegisterStoredcumentDetail(ViewSet):
    def list(self,request):
        query=Vendor_store_document.objects.all()
        serializer=VendorRegStodcuDetSerializers(query,many=True)
        vrd={'VendorRegisterStoredcumentDetail':serializer.data,'response_code':200,'comments':'all list',"status": True}
        return Response(vrd)
    def create(self,request):
        datas=request.data
        email=datas.get('email')
        store_seller_aadhar =datas.get('aadhar_number')
        store_seller_front_aadhar_image =datas.get('aadhar_image_front')
        store_seller_back_aadhar_image =datas.get('aadhar_image_back')
        store_seller_pancard =datas.get('pancard_number')
        store_seller_pancard_image = datas.get('pancard_image')
        try:
            store_shiping_policy =datas.get('store_shiping_policy')
        except:
            store_shiping_policy=None
        store_seller_gst =datas.get('store_gst')
        try:
            store_return_policy =datas.get('store_return_policy')
        except:
            store_return_policy = None

        store_bank_account_number =datas.get('bank_account_number')
        store_bank_name =datas.get('bank_name')
        store_bank_ifsc =datas.get('bank_ifsc')
        store_bank_passbook =datas.get('bank_passbook_image')
        store_seller_razorpay_id =datas.get('razorpay_id')
        store_seller_aadhar =datas.get('aadhar_number')
        store_seller_front_aadhar_image =datas.get('aadhar_image_front')
        store_seller_back_aadhar_image =datas.get('aadhar_image_back')
        store_seller_pancard =datas.get('pancard_number')
        store_seller_pancard_image =datas.get('pancard_image')
        try:
            store_shiping_policy =datas.get('store_shiping_policy')
        except:
            store_shiping_policy=None
        store_seller_gst =datas.get('store_gst')
        try:
            store_return_policy =datas.get('store_return_policy')
        except:
            store_return_policy = None

        store_bank_account_number =datas.get('bank_account_number')
        store_bank_name =datas.get('bank_name')
        store_bank_ifsc =datas.get('bank_ifsc')
        store_bank_passbook =datas.get('bank_passbook_image')
        store_seller_razorpay_id = datas.get('razorpay_id')
        try:

            user_instance = User.objects.get(username=email)
            store_document = Vendor_store_document(user=user_instance,store_seller_aadhar=store_seller_aadhar,store_seller_front_aadhar_image=store_seller_front_aadhar_image,
                                                  store_seller_back_aadhar_image=store_seller_back_aadhar_image,store_seller_pancard=store_seller_pancard,
                                                   store_seller_pancard_image=store_seller_pancard_image,store_shiping_policy=store_shiping_policy,store_seller_gst=store_seller_gst,
                                                  store_return_policy=store_return_policy,store_bank_account_number=store_bank_account_number,store_bank_name=store_bank_name,
                                                  store_bank_ifsc=store_bank_ifsc,store_bank_passbook=store_bank_passbook,store_seller_razorpay_id=store_seller_razorpay_id)
            store_document.save()
            response_data = {'response_code':status.HTTP_201_CREATED,'comments':'Store Details successful register',"status": True}
            return Response(response_data)

        except:
            response_data = {'response_code':status.HTTP_400_BAD_REQUEST,'comments':'Vendor is not register',"status": False}
            return Response(response_data)

###Category.objects.all() all list jayega
class CategoryALL(ViewSet):
    def list(self,request):
        query=Category.objects.all()
        serializers=CategorySerializer_only(query,many=True)
        cat={'category':serializers.data,'response_code':200,'comments':'all list',"status": True}
        return Response(cat)
    def create(self,request):
        name=request.data.get('name')
        if name=='':
            response_data = {'response_code':200,'comments':'Category is required',"status": False}
            return Response(response_data)
        else:
            cat=Category(name=name)
            cat.save()
            response_data = {'response_code':200,'comments':'Category Created',"status": True}
            return Response(response_data)
    
    def update(self,request,id=None):
        name1=request.data.get('name')
        try:
            cat_inst=Category.objects.get(id=id)
            cat_inst.name=name1
            cat_inst.save()
            response_data = {'response_code':200,'comments':'Category updated',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'Category id not exist',"status": False}
            return Response(response_data)
    def destory(self,request,id=None):
        try:
            cat_inst=Category.objects.get(id=id)
            cat_inst.delete()
            response_data = {'response_code':200,'comments':'Category deleted',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'Category id not exist',"status": False}
            return Response(response_data)

class SubcategoryALL(ViewSet):
    def list(self,request):
        
        sub_obje=Subcategory.objects.all()
        serilizers=SubcategorySerializer_only(sub_obje,many=True)
        subcat={'subcategry':serilizers.data,'response_code':200,'comments':'all list',"status": True}
        return Response(subcat)
    def create(self,request):
        C_id=request.data.get('category_id')
        try:
            if C_id=='':
                response_data = {'response_code':200,'comments':'all fields are required',"status": True}
                return Response(response_data)
            else:
                cat_inst=Category.objects.filter(id__in=C_id)
                sub_obj=Subcategory.objects.filter(category__in=cat_inst)
                if sub_obj:
                    dat_dict={}
                    data_list=[]
                    for x in sub_obj:
                        dat_dict={'category_id':x.category.id,'category_name':x.category.name,
                        'subcategory_id':x.id,'subcategory_name':x.name,'subcategory_image':str(x.image)}
                        data_list.append(dat_dict)
                    shop_dict={"subcategory_details":data_list,'response_code':200,'comments':'all list',"status": True}
                    return Response(shop_dict)
                else:
                    response_data = {'response_code':200,'comments':'subcategory is not exsit',"status": False}
                    return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'Category is not exsit',"status": False}
            return Response(response_data)


class SubSubcategoryAll(ViewSet):
    def list(self,request):
        query=Brands.objects.all()
        ser=SubSubcategorySerializer_only(query,many=True)
        subsub={'brands_list':ser.data,'response_code':200,'comments':'all list',"status": True}
        return Response(subsub)
    def create(self,request):
        s_id=request.data.get('subcategory_id')
        try:
            if s_id=='':
                response_data = {'response_code':200,'comments':'all fields are required',"status": True}
                return Response(response_data)
            else:
                sub_obj=Subcategory.objects.filter(id__in=s_id)
                brand_obj=Brands.objects.filter(subcategory__in=sub_obj)
                if brand_obj:
                    dat_dict={}
                    data_list=[]
                    for x in brand_obj:
                        dat_dict={'subcategory_id':x.subcategory.id,'subcategory_name':x.subcategory.name,
                           'brand_id':x.id,'brand_name':x.name,'brand_image':str(x.image)}
                        data_list.append(dat_dict)
                    shop_dict={"products_details":data_list,'response_code':200,'comments':'all list',"status": True}
                    return Response(shop_dict)
                else:
                    response_data = {'response_code':200,'comments':'brand is not exsit',"status": False}
                    return Response(response_data)

        except:
            response_data = {'response_code':200,'comments':'subcategory is not exsit',"status": False}
            return Response(response_data)
        

        

############################start login api ####################
class Login_check(ViewSet):
    def create(self,request):
        data=request.data
        email1=data.get('email')
        password1=data.get('password')
        user1=authenticate(username=email1,password=password1)
        # if user1.check_password(password1):
        if user1 is not None:
            print('----')
            try:
                print('--#333--')
                user_instance = User_register.objects.get(user=user1)
                print('----')
                if user_instance.status==True:
                    user_det=User.objects.get(username=email1)
                    user_reg=User_register.objects.get(user=user_det)
                    sending_data=[]
                    userdata={'id':user_det.id,'email':user_det.username,'first_name':user_det.first_name,'last_name':user_det.last_name,'image':str(user_reg.profile_pic),'address':user_reg.address,'phone':user_reg.mobile,'status':user_reg.status,'gender':user_reg.gender,'latitude':user_reg.latitude,'longitude':user_reg.longitude}
                    sending_data.append(userdata)
                    response_data = {'user_data':sending_data,'response_code':200,'comments':'user exist',"status": True}
                    return Response(response_data) 
                else:
                    response_data = {'response_code':200,'comments':'You are Block by Admin',"status": False}
                    return Response(response_data)
            except:
                
                vendor_instance = Vendor_registration.objects.get(user=user1)
                if vendor_instance.store_status==True:

                    user_det=User.objects.get(username=email1)
                    vender=Vendor_registration.objects.get(user=user_det)
                    serdata=VendorRegisterSerializers(vender)
                    response_data = {'user_data':serdata.data,'response_code':200,'comments':'login is successful',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'You are Block by Admin',"status": False}
                    return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'user is not match',"status": False}
            return Response(response_data) 
        ####################end login api ####################
############################start logout api ####################


class Logout_check(ViewSet):
    def list(self,request):
        logout(request)
        response_data = {'response_code':200,'comments':'logout is successful',"status": True}
        return Response(response_data)     

class Contactall(ViewSet):
    def create(self,request):
        datas=request.data
        name1=datas.get('name')
        email1=datas.get('email')
        mobile1=datas.get('mobile')
        message1=datas.get('message')
        try:
            cont_qr=contact(name=name1,email=email1,mobile=mobile1,message=message1)
            cont_qr.save()
            response_data = {'response_code':200,'comments':'contact is created',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'contacts is not none',"status": False}
            return Response(response_data) 
    def list(self,request):
        query=contact.objects.all()
        serilizer=ContactSerializer(query,many=True)
        contact={'contact':serilizer.data,'response_code':200,'comments':'all list',"status": True}
        return Response(contact)
    def destory(self,request,id=None):
        try:
            dt=contact.objects.get(id=id)
            dt.delete()
            return Response('contact is deleted')
        except contact.DoesNotExist:
            return Response('contact is not available')


class BannerALL(ViewSet):
    def list(self,request):
        query=Banner.objects.all()
        ser=BannerSerializer(query,many=True)
        banner={'Banner':ser.data,'response_code':200,'comments':'all list',"status": True}
        return Response(banner)

class Bottom_BannerAll(ViewSet):
    def list(self,request):
        query=Bottom_Banner.objects.all()
        ser=Bottom_BannerSerializer(query,many=True)
        banner={'bottom_banner':ser.data,'response_code':200,'comments':'all list',"status": True}
        return Response(banner)




# ################################### mail sendin function ##################
def send_conformation_email(request,rand_otp):
    email = request.session.get('email')
    if email:
        subject = "Welcome To AVPL"
        message = "This is your OTP "+str(rand_otp)
        recepient = str(email)
        #html_message = render_to_string('home/send_order_report.html', context)
        #plain_message = strip_tags(html_message)
        #from_email = settings.EMAIL_HOST_USER
        #to = email
        send_mail(subject, message,EMAIL_HOST_USER,[recepient],fail_silently=False)
    else:
        return False



################################### end mail sendin function ##################


class Forget_password(ViewSet):
    def create(self,request):
        data=request.data
        request.session['email'] =data.get('email')
        email = request.session.get('email')
        print(email)
        try:

            check_email = User.objects.get(username=email)
            OTP = randint(1111, 9999)
            if check_email:
                    try:
                        otp = Otp.objects.get(email=email)
                        otp.otp = OTP
                        otp.save()
                    except:
                        otp = Otp(email=email, otp=OTP)
                        otp.save()
                    send_conformation_email(request,OTP)
                    response_data = {'response_code':200,'comments':'otp is send to mail',"status": True}
                    return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'email is not register',"status": True}
            return Response(response_data)

class Forget_Password_Verify_Otp(ViewSet):
    def create(self,request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        password1 = request.data.get('password')
        password2 = request.data.get('repassword')
        otp_featch = Otp.objects.get(email=email)
        print(password1,password2,otp,email)
        if otp_featch.otp == otp:
            if password1 == password2:
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                # compiling regex
                match_re = re.compile(reg)
                # searching regex
                res = re.search(match_re, password1)
                if res:
                    user_featch  = User.objects.get(username=email)
                    user_featch.password = make_password(password1)
                    user_featch.save()
                    response_data = {'response_code':200,'comments':'password changed successfully..',"status": True}
                    return Response(response_data)
                else:
                    response_data = {'response_code':200,'comments':'Passowrd must be strong..or min 8 char',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'Password and confirm password not match..',"status": False}
                return Response(response_data)
        else:
            response_data = {'response_code':200,'comments':'Otp not Vaild..',"status": False}
            return Response(response_data)

class Forget_Password_Resend_Otp(ViewSet):
    def create(self,request):
        email = request.session.get('email')
        try:
            otp = randint(1111, 9999)
            otp_update = Otp.objects.get(email=email)
            otp_update.otp = otp
            otp_update.save()
            send_conformation_email(request,otp)
            response_data = {'response_code':200,'comments':'Resend OTP Successfully on your register Email..',"status": True}
            return Response(response_data)
        except:
            response_data = {'response_code':200,'comments':'apply Forget_Password_Verify_Otp ',"status": False}
            return Response(response_data)



################### end forget resend otp #######



class Addres_Search_For_Shop(ViewSet):
    def create(self,request):
        category = request.data.get('category')
        address = request.data.get('address')
        if address != '':
                gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
                add_lat_long = gmaps.geocode(address)
                user_lat = add_lat_long[0]['geometry']['location']['lat']
                user_lng = add_lat_long[0]['geometry']['location']['lng']
                newport_ri = (user_lat, user_lng)
                print('useraddrs',newport_ri)
                li = []
                print('code run hua yha tk ab pta  nhi....')
                obj = Vendor_Store_detail.objects.all()
                for x in obj:
                    cleveland_oh = (x.store_latitude, x.store_longitude)
                    print('shop',cleveland_oh)
                    c = geodesic(newport_ri, cleveland_oh).miles
                    Km = c / 0.62137
                    print('km',Km)
                    if Km <=10:
                        user_instance = User.objects.get(username=x.user)
                        li.append(user_instance)
                if category:
                    shop = Vendor_Store_detail.objects.filter(user__in=li).filter(store_category=category)
                    if shop:
                        vend_serlizer=VendorStoreDetailSerializers(shop,many=True)
                        # category = Category.objects.all()
                        # serilizer=CategorySerializer_only(category,many=True)
                        dat={'shop':vend_serlizer.data,'response_code':200,'comments':'all list',"status": True}
                        return Response(dat)
                    else:
                        # category = Category.objects.all()
                        # serilizer=CategorySerializer_only(category,many=True)
                        dat={'response_code':200,'comments':'No store found Search any other address',"status": False}
                        return Response(dat)
                else:
                    shop = Vendor_Store_detail.objects.filter(user__in=li)
                    if shop:
                        vend_serlizer=VendorStoreDetailSerializers(shop,many=True)
                        # category = Category.objects.all()
                        # serilizer=CategorySerializer_only(category,many=True)
                        dat={'shop':vend_serlizer.data,'response_code':200,'comments':'all list',"status": True}
                        return Response(dat)
                    else:
                        # category = Category.objects.all()
                        # serilizer=CategorySerializer_only(category,many=True)
                        dat={'response_code':200,'comments':'No store found Search any other address',"status": False}
                        return Response(dat)

        else:
            dat={'response_code':200,'comments':'enter address',"status": False}
            return Response(dat)
    


class Addres_Search_For_Shop_after_Login(ViewSet):
    def create(self,request):
        email1=request.data.get('user_email')
        category = request.data.get('category')
        address = request.data.get('address')
        
        if address != '':
            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
            add_lat_long = gmaps.geocode(address)
            user_lat = add_lat_long[0]['geometry']['location']['lat']
            user_lng = add_lat_long[0]['geometry']['location']['lng']
            try:

                user_instance = User.objects.get(username =email1)
                try: 
                    fatch_random_address = random_address.objects.get(user=user_instance)
                    if fatch_random_address:
                        fatch_random_address.address = address
                        fatch_random_address.latitude = user_lat
                        fatch_random_address.longitude = user_lng
                        fatch_random_address.save()
                        print('i am update')
                except:
                    raandom_address = random_address(user=user_instance,address=address,latitude=user_lat,longitude=user_lng)
                    raandom_address.save()
                    # return redirect('/')
                # obj = User.objects.get(username =email1)
                adrs = random_address.objects.get(user=user_instance)
                lat = adrs.latitude
                lng = adrs.longitude
                objs = Vendor_Store_detail.objects.all()
                newport_ri = (lat, lng)
                li = []
                print('code run hua yha tk ab pta  nhi....')
                for x in objs:
                    # print(x.store_latitude,x.store_longitude)
                    cleveland_oh = (x.store_latitude, x.store_longitude)
                    c = geodesic(newport_ri, cleveland_oh).miles
                    Km = c / 0.62137
                    if Km <=10:
                        user_instance = User.objects.get(username=x.user)
                        li.append(user_instance)
                if category:
                    shop = Vendor_Store_detail.objects.filter(user__in=li).filter(store_category=category)
                    if shop:
                        vend_serlizer=VendorStoreDetailSerializers(shop,many=True)
        
                        dat={'shop': vend_serlizer.data,'response_code':200,'comments':'all list',"status": True}
                        return Response(dat)
                    else:

                        dat={'response_code':200,'comments':'shop is not in your location',"status": False}
                        return Response(dat)
                else:
                    shop = Vendor_Store_detail.objects.filter(user__in=li)
                    if shop:
                        vend_serlizer=VendorStoreDetailSerializers(shop,many=True)
                        dat={'shop': vend_serlizer.data, 'response_code':200,'comments':'all list',"status": True}
                        return Response(dat)
                    else:
                        dat={'response_code':200,'comments':'shop is not in your location',"status": False}
                        return Response(dat)
            except:
                dat={'response_code':200,'comments':'user not exist',"status": False}
                return Response(dat)

        else:
            dat={'response_code':200,'comments':'enter address',"status": False}
            return Response(dat)








class ProductALL(ViewSet):
    def list(self,request):
        product_obj=Product.objects.all()
        if product_obj:

            dat_dict={}
            data_list=[]

            for x in product_obj:
                dat_dict={'vendor_id':x.user.id,'vendor_email':x.user.username,'first_name':x.user.first_name,'last_name':x.user.last_name,
                'category_id':x.category.id,'category_name':x.category.name,'subcategory_id':x.subcategory.id,'subcategory_name':x.subcategory.name,
                'brand_id':x.brand_name.id,'brand_name':x.brand_name.name,'product_id':x.id,'product_title':x.title,'product_price':x.price,'product_discount_percent':x.discount_percent,
                'product_gst_percent':x.gst_percent,'product_variant':x.variant,
                'product_image':str(x.image),'product_status':x.status
                }
                data_list.append(dat_dict)
            shop_dict={"product_details":data_list,'response_code':200,'comments':'all list',"status": True}
           
            return Response(shop_dict)
        else:
            shop_dict={'response_code':200,'comments':'no details of shop',"status": False}
            return Response(shop_dict)
    def create(self,request):
        stor_id=request.data.get('stor_id')
        dat_dict={}
        data_list=[]
        if stor_id:
            stor_inst=Vendor_Store_detail.objects.filter(id__in=stor_id)
            if stor_inst:
                product_obj=Product.objects.filter(stor_details__in=stor_inst)
                if product_obj:
                    for x in product_obj:
                        dat_dict={'vendor_id':x.user.id,'vendor_email':x.user.username,'first_name':x.user.first_name,'last_name':x.user.last_name,
                            'category_id':x.category.id,'category_name':x.category.name,'subcategory_id':x.subcategory.id,'subcategory_name':x.subcategory.name,
                            'brand_id':x.brand_name.id,'brand_name':x.brand_name.name,'product_id':x.id,'product_title':x.title,'product_price':x.price,'product_discount_percent':x.discount_percent,
                            'product_gst_percent':x.gst_percent,'product_variant':x.variant,
                                'product_image':str(x.image),'product_status':x.status}
                        data_list.append(dat_dict)
                    shop_dict={"products_details":data_list,'response_code':200,'comments':'all list',"status": True}
                    return Response(shop_dict)
                else:
                    response_data = {'response_code':200,'comments':'product is not exsit',"status": False}
                    return Response(response_data)
            else:
                response_data = {'response_code':200,'comments':'stor is not exsit',"status": False}
                return Response(response_data)

        else:
            response_data = {'response_code':200,'comments':'all fields required',"status": False}
            return Response(response_data)
        


    


        

class ImageAll(ViewSet):
    def list(self,request):
        image_obj=Images.objects.all()
        if image_obj:
            data_list=[]
            data_dict={}
            for x in image_obj:
                data_dict={'product_id':x.product.id,'image_id':x.id,'image_title':x.title,'image_url':x.image}
                data_list.append(data_dict)
            pt={'image_details':data_list,'response_code':200,'comments':'all list',"status": True}
            return Response(pt)
        else:
            res={'response_code':200,'comments':'no list',"status": False}
            return Response(res)


class ColorSizeBrandAll(ViewSet):
    def list(self,request):
        color_obj=Color.objects.all()
        size_obje=Size.objects.all()
        brand_obj=Brands.objects.all()
        color_dict={}
        color_list=[]
        size_dict={}
        size_list=[]
        brand_dict={}
        brand_list=[]
        for x in color_obj:
            color_dict={'color_id':x.id,'color_name':x.name,'color_code':x.code}
            color_list.append(color_dict)
        for y in size_obje:
            size_dict={'size_id':y.id,'size_name':y.name,'size_code':y.code}
            size_list.append(size_dict)
        for z in brand_obj:
            brand_dict={'brand_id':z.id,'brand_name':z.name,'brand_image':str(z.image)}
            brand_list.append(brand_dict)

        ct={'brand_details':brand_list,"color_details":color_list,'size_details':size_list,'response_code':200,'comments':'all list',"status": True}
        return Response(ct)
        

class VariantsAll(ViewSet):
    def create(self,request):
        brand_id=request.data.get('brand_id')
        size_id=request.data.get('size_id')
        color_id=request.data.get('color_id')
        try:
            brand_objet=Brands.objects.filter(id__in=brand_id)
            product_obj=Product.objects.filter(brand_name__in=brand_objet)
            size_obj=Size.objects.filter(id__in=size_id)
            color_obj=Color.objects.filter(id__in=color_id)
            data_dict={}
            data_list=[]
            if brand_id and size_id and color_id:
                vernt_obj=Variants.objects.filter(product__in=product_obj).filter(size__in=size_obj).filter(color__in=color_obj)
                if vernt_obj:
                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                         'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)

            elif brand_id and size_id:
                vernt_obj=Variants.objects.filter(product__in=product_obj).filter(size__in=size_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            
            elif size_id and color_id:
                vernt_obj=Variants.objects.filter(size__in=size_obj).filter(color__in=color_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
                
            elif brand_id and color_id :
                vernt_obj=Variants.objects.filter(product__in=product_obj).filter(color__in=color_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            elif brand_id:
                vernt_obj=Variants.objects.filter(product__in=product_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            elif size_id:
                vernt_obj=Variants.objects.filter(size__in=size_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            elif color_id:
                vernt_obj=Variants.objects.filter(color__in=color_obj)
                if vernt_obj:

                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                        'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                        'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                        'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                        }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            else:
                vernt_obj=Variants.objects.all()
                for x in vernt_obj:
                    data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                    'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                    'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                    'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                    }
                    data_list.append(data_dict)
                dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'no list',"status": False} 
            return Response(dt)

           
class VariantbySubcategryStor(ViewSet):
    def create(self,request):
        stor_id=request.data.get('stor_id')
        subcat_id=request.data.get('subcat_id')
        try:
            stor_inst=Vendor_Store_detail.objects.filter(id__in=stor_id)
            subcat_inst=Subcategory.objects.filter(id__in=subcat_id)
            data_dict={}
            data_list=[]
            if stor_id and subcat_id:
                product_obj=Product.objects.filter(stor_details__in=stor_inst).filter(subcategory__in=subcat_inst)
                vernt_obj=Variants.objects.filter(product__in=product_obj)
                if vernt_obj:
                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                                'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                                'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                                'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                                }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            elif stor_id:
                product_obj=Product.objects.filter(stor_details__in=stor_inst)
                vernt_obj=Variants.objects.filter(product__in=product_obj)
                if vernt_obj:
                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                                'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                                'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                                'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                                }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no list',"status": False} 
                    return Response(dt)
            elif subcat_id:
                product_obj=Product.objects.filter(subcategory__in=subcat_inst)
                vernt_obj=Variants.objects.filter(product__in=product_obj)
                if vernt_obj:
                    for x in vernt_obj:
                        data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                                'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                                'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                                'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                                }
                        data_list.append(data_dict)
                    dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                    return Response(dt)
            else:
                vernt_obj=Variants.objects.all()
                for x in vernt_obj:
                    data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                    'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                    'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                    'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                    }
                    data_list.append(data_dict)
                dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'no list',"status": False} 
            return Response(dt)



class VariantbySubcategry(ViewSet):
        def create(self,request):
            email1=request.data.get('user_email')
            subcat_id = request.data.get('subcat_id')
            try:
                obj = User.objects.get(username=email1)
                adrs = random_address.objects.get(user=obj)
                lat = adrs.latitude
                lng = adrs.longitude
                newport_ri = (lat, lng)
                objs = Vendor_Store_detail.objects.all()
                li = []
                for x in objs:
                    # print(x.store_latitude,x.store_longitude)
                    cleveland_oh = (x.store_latitude, x.store_longitude)
                    c = geodesic(newport_ri, cleveland_oh).miles
                    Km = c / 0.62137
                    if Km <=10:
                        user_instance = User.objects.get(username=x.user)
                        li.append(user_instance)
                if subcat_id:
                    shop = Vendor_Store_detail.objects.filter(user__in=li)
                    try:
                        subcat_inst=Subcategory.objects.get(id=subcat_id)
                        data_dict={}
                        data_list=[]
                        if subcat_inst:
                            product_obj=Product.objects.filter(subcategory=subcat_inst).filter(stor_details__in=shop)
                            vernt_obj=Variants.objects.filter(product__in=product_obj)
                            if vernt_obj:
                                for x in vernt_obj:
                                    data_dict={'variant_id':x.id,'variant_title':x.title,'variant_description':x.description,'variant_image_fornt':str(x.image_fornt),'variant_image_back':str(x.image_back),'variant_image_side':str(x.image_side),
                                            'variant_quantity':x.quantity,'variant_price':x.price,'variant_weight':x.weight,'variant_point_value':x.point_value,
                                            'product_id':x.product.id,'product_title':x.product.title,'product_price':x.product.price,'product_brand_id':x.product.brand_name.id,'product_brand_name':x.product.brand_name.name,'product_subcategory_id':x.product.subcategory.id,'product_subcategory_name':x.product.subcategory.name,'product_category_id':x.product.category.id,'product_category_name':x.product.category.name,'vandor_id':x.product.user.id,'vendor_email':x.product.user.username,
                                            'variant_color_id':x.color.id,'variant_color_name':x.color.name,'variant_size_id':x.size.id,'variant_size_name':x.size.name
                                            }
                                    data_list.append(data_dict)
                                dt={'variant_details':data_list,'response_code':200,'comments':'all list',"status": True} 
                                return Response(dt)
                            else:
                                dt={'response_code':200,'comments':'no variant list',"status": False} 
                                return Response(dt)
                    except:
                        dt={'response_code':200,'comments':'no  subcategry list',"status": False} 
                        return Response(dt)

                else:
                    dt={'response_code':200,'comments':'no   list',"status": False} 
                    return Response(dt) 
            except:
                dt={'response_code':200,'comments':'no id',"status": False} 
                return Response(dt)

        
        
# class UserCartAdd(ViewSet):
#     def create(self,request):
#         user_email=request.data.get('user_email')
#         variant_id=request.data.get('variant_id')
#         quantity=request.data.get('quantity')
#         final_price=request.data.get('final_price')
#         if user_email=='' or variant_id=='':
#             dt={'response_code':200,'comments':'all fields are requires',"status": False} 
#             return Response(dt)
#         try:
#             data_dict={}
#             data_list=[]
#             user_instace = User.objects.get(username=user_email)
#             if user_instace:
#                 try:
#                     varient_featch=Variants.objects.get(id=variant_id)
#                     vendor_inst_by_user = User.objects.get(username=varient_featch.product.user)
#                     vendor_store_detail_inst = Vendor_Store_detail.objects.get(user=vendor_inst_by_user)
#                     cart_data_featch = UserCart.objects.filter(user=user_instace,cart_status=False)
#                     if cart_data_featch:
#                         ct_fatch=UserCart.objects.filter(store_user = vendor_store_detail_inst)
#                         if ct_fatch:
#                             if varient_featch.quantity >= int(1):
#                                 try:
#                                     cart_featch = UserCart.objects.filter(user=user_instace,cart_status=False).get(variant_id = varient_featch)
#                                     if cart_featch.cart_status == False:
#                                         cart_featch.quantity = cart_featch.quantity + int(1)
#                                         cart_featch.final_price = cart_featch.quantity * varient_featch.price
#                                         cart_featch.save()
#                                         cart_data =  UserCart.objects.get(variant_id = varient_featch,user=user_instace,cart_status=False)
#                                         data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
#                                         data_list.append(data_dict)
#                                         dt={'usercart_details':data_list,'response_code':200,'comments':'item add ',"status": True} 
#                                         return Response(dt)
#                                     else:
#                                         final_price = int(1) * varient_featch.price
#                                         cart = UserCart(user=user_instace, variant_id=varient_featch, quantity=1,
#                                                         store_user=vendor_store_detail_inst, final_price=final_price)
#                                         cart.save()
#                                         cart_data = UserCart.objects.get(variant_id = varient_featch,user=user_instace)
#                                         data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
#                                         data_list.append(data_dict)
#                                         dt={'usercart_details':data_list,'response_code':200,'comments':'cart add else',"status": True} 
#                                         return Response(dt)
#                                 except:
#                                     final_price =int(1) * varient_featch.price
#                                     cart = UserCart(user=user_instace,variant_id=varient_featch,quantity=1,store_user=vendor_store_detail_inst,final_price=final_price)
#                                     cart.save()
#                                     cart_data =UserCart.objects.get(variant_id = varient_featch,user=user_instace,cart_status=False)
#                                     data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
#                                     data_list.append(data_dict)
#                                     dt={'usercart_details':data_list,'response_code':200,'comments':'cart add first time',"status": True} 
#                                     return Response(dt)
#                             else:
#                                 dt={'response_code':200,'comments':'You select maximum quantity select between left quantity ',"status": False} 
#                                 return Response(dt)
#                         else:
#                             dt={'response_code':200,'comments':'First you need to cart clear then you shop by another store ',"status": False} 
#                             return Response(dt)
                        
#                 except:
#                     dt={'response_code':200,'comments':'no variant id',"status": False} 
#                     return Response(dt)
#         except:
#             dt={'response_code':200,'comments':'user is not register',"status": False} 
#             return Response(dt)

class UserCartAdd(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        variant_id=request.data.get('variant_id')
        quantity=request.data.get('quantity')
        final_price=request.data.get('final_price')
        if user_email=='' or variant_id=='':
            dt={'response_code':200,'comments':'all fields are requires',"status": False} 
            return Response(dt)
        try:
            data_dict={}
            data_list=[]
            user_instace = User.objects.get(username=user_email)
            if user_instace:
                try:
                    varient_featch=Variants.objects.get(id=variant_id)
                    vendor_inst_by_user = User.objects.get(username=varient_featch.product.user)
                    vendor_store_detail_inst = Vendor_Store_detail.objects.get(user=vendor_inst_by_user)
                    print(vendor_store_detail_inst)
                    try:
                        cart_data_featch = UserCart.objects.filter(user=user_instace,cart_status=False)
                        print('cart_data_featch',cart_data_featch)
                        # if cart_data_featch:
                        try:
                            ct_fatch=UserCart.objects.filter(store_user = vendor_store_detail_inst)
                            print('ct_fatch',ct_fatch)
                            print('ct_fatch',ct_fatch)
                            # if ct_fatch:
                            if varient_featch.quantity >= int(1):
                                try:
                                    print('tryyyyy')
                                    cart_featch = UserCart.objects.filter(user=user_instace,cart_status=False).get(variant_id = varient_featch)
                                    if cart_featch.cart_status == False:
                                        cart_featch.quantity = cart_featch.quantity + int(1)
                                        cart_featch.final_price = cart_featch.quantity * varient_featch.price
                                        cart_featch.save()
                                        cart_data =  UserCart.objects.get(variant_id = varient_featch,user=user_instace,cart_status=False)
                                        data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
                                        data_list.append(data_dict)
                                        dt={'UserCart_details':data_list,'response_code':200,'comments':'item add ',"status": True} 
                                        return Response(dt)
                                    else:
                                        final_price = int(1) * varient_featch.price
                                        cart = UserCart(user=user_instace, variant_id=varient_featch, quantity=1,
                                                        store_user=vendor_store_detail_inst, final_price=final_price)
                                        cart.save()
                                        cart_data = UserCart.objects.get(variant_id = varient_featch,user=user_instace)
                                        data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
                                        data_list.append(data_dict)
                                        dt={'UserCart_details':data_list,'response_code':200,'comments':'cart add else',"status": True} 
                                        return Response(dt)
                                except:
                                    print('excccccccccc')
                                    final_price =int(1) * varient_featch.price
                                    cart = UserCart(user=user_instace,variant_id=varient_featch,quantity=1,store_user=vendor_store_detail_inst,final_price=final_price)
                                    cart.save()
                                    cart_data =UserCart.objects.get(variant_id = varient_featch,user=user_instace,cart_status=False)
                                    data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
                                    data_list.append(data_dict)
                                    dt={'UserCart_details':data_list,'response_code':200,'comments':'cart add first time',"status": True} 
                                    return Response(dt)
                            else:
                                dt={'response_code':200,'comments':'You select maximum quantity select between left quantity ',"status": False} 
                                return Response(dt)
                        except:
                            dt={'response_code':200,'comments':'First you need to cart clear then you shop by another store ',"status": False} 
                            return Response(dt)
                    except:
                        print('statements run here...')
                        final_price = int(1) * varient_featch.price
                        cart = UserCart(user=user_instace,variant_id=varient_featch,quantity=1,store_user=vendor_store_detail_inst,final_price=final_price)
                        cart.save()
                        cart_data =UserCart.objects.get(variant_id = varient_featch,user=user_instace,cart_status=False)
                        data_dict={'variant_id':cart_data.variant_id.id,'quantity':cart_data.quantity,'final_price':cart_data.final_price}
                        data_list.append(data_dict)
                        dt={'UserCart_details':data_list,'response_code':200,'comments':'except new add cart ',"status": True} 
                        return Response(dt)
                    
                except:
                    dt={'response_code':200,'comments':'no variant id',"status": False} 
                    return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)

class CartShow(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:  
            user_instance = User.objects.get(username=user_email)
            print(user_instance)
            if user_instance:
                cart_featch = UserCart.objects.filter(user=user_instance,cart_status=False)
                data_dict={}
                data_list=[]
                sub_total_price = 0
                if cart_featch:
                    for x in cart_featch:
                        data_dict={'usercart_id':x.id,'usercart_user':x.user.username,'variant_id':x.variant_id.id,'variants_title':x.variant_id.title,'variants_image':str(x.variant_id.image_fornt),'variants_image_back':str(x.variant_id.image_back),'variants_description':x.variant_id.description,'variants_quantity':x.variant_id.quantity,'variants_price':x.variant_id.price,'variants_weight':x.variant_id.weight,'variants_point_value':x.variant_id.point_value,'variants_color_id':x.variant_id.color.id,'variants_color_name':x.variant_id.color.name,'variants_size_id':x.variant_id.size.id,'variants_size_name':x.variant_id.size.name,'product_id':x.variant_id.product.id,'product_title':x.variant_id.product.title,'quantity':x.quantity,'stor_id':x.store_user.id,'store_name':x.store_user.store_name,'store_address':x.store_user.store_address,'final_price':x.final_price,'cart_status':x.cart_status}
                        data_list.append(data_dict)
                        sub_total_price = x.final_price + sub_total_price
                    shipping =15.0
                    grand_total = sub_total_price + shipping
                    dt={'cart_details':data_list,'sub_total':sub_total_price,'shipping':shipping,"grand_total":grand_total,'response_code':200,'comments':'cart and shoping details',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'on order in usercart',"status": False} 
                    return Response(dt)

        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)

class CartRemove(ViewSet):
    def create(self,request):
        usercart_id=request.data.get('usercart_id')
        if usercart_id=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            ct =UserCart.objects.get(pk=usercart_id)
            ct.delete()
            dt={'response_code':200,'comments':'order is remove',"status": True} 
            return Response(dt)
        except:
            dt={'response_code':200,'comments':'no cart id',"status": False} 
            return Response(dt)
class CartPlus(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        variant_id=request.data.get('variant_id')
        if user_email=='' or variant_id=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            data_dict={}
            data_list=[]
            user_instance = User.objects.get(username =user_email)
            if user_instance:
                try:
                    product_featch = Variants.objects.get(id=variant_id)
                    if product_featch:
                        carts = UserCart.objects.filter(user=user_instance,cart_status=False).get(variant_id=variant_id)
                        if product_featch.quantity > carts.quantity:
                            carts.quantity = carts.quantity + 1
                            carts.final_price = carts.quantity * product_featch.price
                            carts.save()
                            user_cart=UserCart.objects.get(variant_id=variant_id)
                            data_dict={'UserCart-id':user_cart.id,'varint_id':user_cart.variant_id.id,'varint_quantity':user_cart.quantity,'varint_title':user_cart.variant_id.title,'product_id':user_cart.variant_id.product.id}
                            data_list.append(data_dict)
                            dt={'cart_details':data_list,'response_code':200,'comments':'product add',"status": True} 
                            return Response(dt)
                        else:
                            user_cart=UserCart.objects.get(variant_id=variant_id)
                            data_dict={'UserCart-id':user_cart.id,'varint_id':user_cart.variant_id.id,'varint_quantity':user_cart.quantity,'varint_title':user_cart.variant_id.title,'product_id':user_cart.variant_id.product.id}
                            data_list.append(data_dict)
                            dt={'cart_details':data_list,'UserCart-id':user_cart.id,'varint_id':user_cart.variant_id.id,'varint_quantity':user_cart.quantity,'varint_title':user_cart.variant_id.title,'product_id':user_cart.variant_id.product.id,'response_code':200,'comments':'You already add maximum quantity',"status": False} 
                            return Response(dt)
                        
                except:
                    dt={'response_code':200,'comments':'no variant id',"status": False} 
                    return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)

class CartMinus(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        variant_id=request.data.get('variant_id')
        if user_email=='' or variant_id=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            data_dict={}
            data_list=[]
            user_instance = User.objects.get(username=user_email)
            if user_instance:
                try:
                    product_featch = Variants.objects.get(id=variant_id)
                    print(product_featch)
                    if product_featch:
                        try:
                            carts = UserCart.objects.filter(user=user_instance,cart_status=False).get(variant_id=variant_id)
                            print('carts',carts)
                            if carts.quantity >= 2:
                                carts.quantity = carts.quantity - 1
                                carts.final_price = carts.quantity * product_featch.price
                                carts.save()
                                user_cart=UserCart.objects.get(variant_id=variant_id)
                                data_dict={'UserCart-id':user_cart.id,'varint_id':user_cart.variant_id.id,'varint_quantity':user_cart.quantity,'varint_title':user_cart.variant_id.title,'product_id':user_cart.variant_id.product.id}
                                data_list.append(data_dict)
                                dt={'cart_details':data_list,'response_code':200,'comments':'cart item  remove',"status": True} 
                                return Response(dt)
                            else:
                                carts.delete()
                                # user_cart=UserCart.objects.get(variant_id=variant_id)
                                # data_dict={'UserCart-id':user_cart.id,'varint_id':user_cart.variant_id.id,'varint_quantity':user_cart.quantity,'varint_title':user_cart.variant_id.title,'product_id':user_cart.variant_id.product.id}
                                # data_list.append(data_dict)
                                dt={'response_code':200,'comments':'usercard delete',"status": True} 
                                return Response(dt)
                        except:
                            dt={'response_code':200,'comments':'usercard not exit',"status": True} 
                            return Response(dt)


                except:
                    dt={'response_code':200,'comments':'no variant id',"status": False} 
                    return Response(dt)

        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)




class WishlistList(ViewSet):

    def create(self,request):
        user_email=request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            user_instance = User.objects.get(username =user_email)
            if user_instance:
                whishlist_featch = Wishlist.objects.filter(user = user_instance)
                data_dict={}
                data_list=[]
                for x in whishlist_featch:
                    product_featch = Variants.objects.get(id=x.variant_id.id)
                    if product_featch:
                        data_dict={'whishlist_id':x.id,'varint_id':product_featch.id,'varint_title':product_featch.title,'varint_description':product_featch.description,'varint_image_fornt':str(product_featch.image_fornt),'varint_price':product_featch.price,'varint_color':product_featch.color.name,'varint_size':product_featch.size.name,'varint_weight':product_featch.weight,'point_value':product_featch.point_value,'after_discount_price':product_featch.after_discount_price,'variant_discount':product_featch.variant_discount}
                        data_list.append(data_dict)
                if data_list:
                    dt={'wishlist':data_list,'response_code':200,'comments':'wishlist details',"status": True} 
                    return Response(dt)
                else:
                    dt={'response_code':200,'comments':'no wishlist details',"status": False} 
                    return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)
        
class WishlistByUser(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        variant_id=request.data.get('variant_id')
        if user_email=='' or variant_id=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            data_dict={}
            data_list=[]
            user_instance = User.objects.get(username=user_email)
            if user_instance:
                try:
                    product_instance = Variants.objects.get(id=variant_id)
                    if product_instance:
                        vendro_inst = User.objects.get(username=product_instance.product.user)
                        vendro_store_inst = Vendor_Store_detail.objects.get(user=vendro_inst)
                        
                        try:
                            whislist_featch = Wishlist.objects.get(variant_id=product_instance)
                            data_dict={'wishlist_id':whislist_featch.id,'varient_id':whislist_featch.variant_id.id,'varient_title':whislist_featch.variant_id.id,'varient_description':whislist_featch.variant_id.description,'image_fornt':str(whislist_featch.variant_id.image_fornt),'varint_price':whislist_featch.variant_id.price,'varint_size':whislist_featch.variant_id.size.name,'varint_color':whislist_featch.variant_id.color.name,'point_value':whislist_featch.variant_id.point_value,'after_discount_price':whislist_featch.variant_id.after_discount_price,'variant_discount':whislist_featch.variant_id.variant_discount}
                            data_list.append(data_dict)
                            dt={'wishlist_details':data_list,'response_code':200,'comments':'This varient already add in your wishlist..',"status": False}
                            return Response(dt)
                        except:
                            whishlist = Wishlist(user=user_instance,variant_id=product_instance,store_user=vendro_store_inst)
                            whishlist.save()
                            whislist_featch = Wishlist.objects.get(variant_id=product_instance)
                            data_dict={'wishlist_id':whislist_featch.id,'varient_id':whislist_featch.variant_id.id,'varient_title':whislist_featch.variant_id.id,'varient_description':whislist_featch.variant_id.description,'image_fornt':str(whislist_featch.variant_id.image_fornt),'varint_price':whislist_featch.variant_id.price,'varint_size':whislist_featch.variant_id.size.name,'varint_color':whislist_featch.variant_id.color.name,'point_value':whislist_featch.variant_id.point_value,'after_discount_price':whislist_featch.variant_id.after_discount_price,'variant_discount':whislist_featch.variant_id.variant_discount}
                            data_list.append(data_dict)
                            dt={'wishlist_details':data_list,'response_code':200,'comments':'add wishlist..',"status": True}
                            return Response(dt)
            
                except:
                    dt={'response_code':200,'comments':'no variant id',"status": False} 
                    return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)
class WishlistRemove(ViewSet):
    def create(self,request):
        wishlist_id=request.data.get('wishlist_id')
        if wishlist_id=='':
            dt={'response_code':200,'comments':'all fields required',"status": False} 
            return Response(dt)
        try:
            whishlist_qr = Wishlist.objects.get(id=wishlist_id)
            if whishlist_qr:
                whishlist_qr.delete()
                dt={'response_code':200,'comments':'wishlist delete',"status": True} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'no wishlist id',"status": False} 
            return Response(dt)
#=======================================================================================
class DeliveryAddressCreate(ViewSet):
    def create(self,request):
        user_email =request.data.get('user_email')
        full_name =request.data.get('full_name')
        phone = request.data.get('phone')
        alternate_phone = request.data.get('alternate_phone')
        email = request.data.get('email')
        address = request.data.get('address')
        city = request.data.get('city')
        pincode = request.data.get('pincode')
        locality = request.data.get('locality')
        landmark = request.data.get('landmark')
        order_mode = request.data.get('order_mode')

        if user_email=='' or full_name=='' or phone==''  or email=='' or address=='' or city=='' or pincode=='' or locality=='' :
            dt={'response_code':200,'comments':'all field reqired',"status": False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            if user_inst:
                deliveryaddres=Delivery_address(user=user_inst,full_name=full_name,phone=phone,alternate_mobile=alternate_phone,
                email=email,address=address,city=city,pincode=pincode,locality=locality,landmark=landmark,order_mode=order_mode )
                deliveryaddres.save()
                dt={'response_code':200,'comments':'delivery address save',"status": True} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user not register',"status": False} 
            return Response(dt)

class DeliveryAddressUpdate(ViewSet):
    def create(self,request):
        user_email =request.data.get('user_email')
        deliver_addr_id=request.data.get('deliver_addr_id')
        full_name =request.data.get('full_name')
        phone = request.data.get('phone')
        alternate_phone = request.data.get('alternate_phone')
        email = request.data.get('email')
        address = request.data.get('address')
        city = request.data.get('city')
        pincode = request.data.get('pincode')
        locality = request.data.get('locality')
        landmark = request.data.get('landmark')
        try:
            user_inst=User.objects.get(username=user_email)
            if user_inst:
                try:
                    delivery_inst=Delivery_address.objects.filter(user=user_inst).get(id=deliver_addr_id)
                    if delivery_inst:
                        delivery_inst.full_name=full_name
                        delivery_inst.phone=phone
                        delivery_inst.alternate_mobile=alternate_phone
                        delivery_inst.email=email
                        delivery_inst.address=address
                        delivery_inst.city=city
                        delivery_inst.pincode=pincode
                        delivery_inst.locality=locality
                        delivery_inst.landmark=landmark
                        delivery_inst.save()
                    dt={'response_code':200,'comments':'delivery address update',"status": True} 
                    return Response(dt)
                except:
                    dt={'response_code':200,'comments':'no delivery address id',"status": False} 
                    return Response(dt)

        except:
            dt={'response_code':200,'comments':'user not register',"status": False} 
            return Response(dt)

class DeliveryAddressDelete(ViewSet):
    def create(self,request):
        user_email =request.data.get('user_email')
        deliver_addr_id=request.data.get('deliver_addr_id')
        if user_email=='' or deliver_addr_id=='':
            dt={'response_code':200,'comments':'all field required',"status": False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            if user_inst:
                try:
                    delivery_inst=Delivery_address.objects.filter(user=user_inst).get(id=deliver_addr_id)
                    delivery_inst.delete()
                    dt={'response_code':200,'comments':'delivery address delete',"status": True} 
                    return Response(dt)
                except:
                    dt={'response_code':200,'comments':'no delivery address id',"status": False} 
                    return Response(dt)

        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)

class DeliveryAddressListByUser(ViewSet):
    def create(self,request):
        user_email =request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all field required',"status": False} 
            return Response(dt)
        data_dict={}
        data_list=[]
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                delivery_query=Delivery_address.objects.filter(user=user_inst)
                for x in delivery_query:
                    data_dict={'delivery_address_id':x.id,'user_id':x.user.id,'user_email':x.user.username,'user_fullname':x.full_name,'user_phone':x.phone,'user_address':x.address,
                    'user_city':x.city,'user_pincode':x.pincode,'order_mode':x.order_mode,'date_time':x.date_time
                    }
                    data_list.append(data_dict)
                dt={'delivery_address_details':data_list,'response_code':200,'comments':'delivery_address all list',"status": True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no delivery address ',"status": False} 
                return Response(dt)

        except:
            dt={'response_code':200,'comments':'user is not register',"status": False} 
            return Response(dt)



########checkout##################        

# class CheckOut(ViewSet):
#     def create(self,request):
#         user_email=request.data.get('user_email')
#         user_inst=User.objects.get(username=user_email)
#         cart_featch = UserCart.objects.filter(user =user_inst,cart_status=False)
#         total_pay = 0
#         store_user=''
#         for x in cart_featch:
#             total_pay = total_pay +x.final_price
#             store_user=x.store_user
#             # print(x.variant_id,'ye varriant hai...')
#             refer_id = request.data.get('refer_id')
#             position= request.data.get('value')
#             name= request.data.get('name')
#             phone= request.data.get('phone')
#             email = request.data.get('email')
#             address= request.data.get('address')
#             city= request.data.get('city')
#             pincode= request.data.get('pincode')
#             locality= request.data.get('locality')
#             landmark = request.data.get('landmark')
#             alternate_phone = request.data.get('alternate_phone')
#             order_mode = request.data.get('order_mode')
            
#             try:     
                
#                 refer_match = Refer_code.objects.get(refercode=refer_id)
#                 print('refer_match',refer_match)
#                 try:
#                     if address != '':
#                         gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
#                         add_lat_long = gmaps.geocode(address)
#                         user_lat = add_lat_long[0]['geometry']['location']['lat']
#                         user_lng = add_lat_long[0]['geometry']['location']['lng']
#                         newport_ri = (user_lat, user_lng)
#                         cleveland_oh = (store_user.store_latitude, store_user.store_longitude)
#                         c = geodesic(newport_ri, cleveland_oh).miles
#                         km = c / 0.62137
#                         print('km',km)
#                         if km <= 10000:
#                             print('kkkkkkkkkkkk')
#                             shipping_address = Delivery_address(user=user_inst,full_name=name, phone=phone,
#                                                                 email=email, address=address, city=city,order_mode=order_mode,
#                                                                 pincode=pincode, locality=locality, landmark=landmark,
#                                                                 alternate_mobile=alternate_phone)
#                             shipping_address.save()
#                             print('shipping_address',shipping_address)
#                             refer_store = Refer_id_store(user=user_inst, refercode=refer_id, position=position)
#                             refer_store.save()
#                             dt={'response_code':200,'comments':'Delivery address save',"status":True} 
#                             return Response(dt)

#                         else:
#                             dt={'response_code':200,'comments':'Delivery are not available to your provided area',"status": False} 
#                             return Response(dt)
#                 except:
#                     dt={'response_code':200,'comments':'Delivery are not available to your provided area-----',"status": False} 
#                     return Response(dt)

#             except:
#                 try:
#                     if address != '':
#                         print('condition ye hai...')
#                         gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
#                         add_lat_long = gmaps.geocode(address)
#                         user_lat = add_lat_long[0]['geometry']['location']['lat']
#                         user_lng = add_lat_long[0]['geometry']['location']['lng']
#                         newport_ri = (user_lat, user_lng)
#                         print('yes i m run here...')
#                         cleveland_oh = (store_user.store_latitude, store_user.store_longitude)
#                         c = geodesic(newport_ri, cleveland_oh).miles
#                         print('yha bhi chal rha..')
#                         km = c / 0.62137
#                         if km <= 1000:
#                             print('ye vali condition chal rha hai...')
#                             shipping_address = Delivery_address(user=user_inst,full_name=name, phone=phone,
#                                                                 email=email, address=address, city=city,order_mode=order_mode,
#                                                                 pincode=pincode, locality=locality, landmark=landmark,
#                                                                 alternate_mobile=alternate_phone)
#                             shipping_address.save()
#                             print('shipping_address',shipping_address)
#                             # ob=shipping_address.id
#                             if order_mode=="Self_Picking":
#                                 dt={'response_code':200,'comments':'self_picking',"status":True} 
#                                 return Response(dt)
#                             else:
#                                 dt={'response_code':200,'comments':'NOT self_picking',"status":False} 
#                                 return Response(dt)
#                         else:
#                             dt={'response_code':200,'comments':'Delivery are not available to your provided area',"status":False} 
#                             return Response(dt)
#                 except:
#                     dt={'response_code':200,'comments':'Delivery are not available to your provided area',"status":False} 
#                     return Response(dt)

# class TimeslotPayment(ViewSet):
#     def create(self,request):
#         user_email=request.data.get('user_email')
#         # time_slot = request.data.get('time_slot')
#         payment_mode= request.data.get('payment')
#         address= request.data.get('address')
#         user_inst=User.objects.get(username=user_email)
#         cart_featch = UserCart.objects.filter(user=user_inst,cart_status=False)
#         total_pay = 0
#         store_user = ''
#         for x in cart_featch:
#             total_pay = total_pay + x.final_price
#             store_user = x.store_user
#         address_instance = Delivery_address.objects.get(address=address)
#         if payment_mode == 'Wallet':
#             print('yes wallet work')
#         elif payment_mode == 'Razorpay':
#             amt = int(total_pay * 100)
#             print(amt)
#             print('run....')
#             client = razorpay.Client(auth=("rzp_test_oh9NnzT3WLdH8D", "2cVCx2C2jgbv9YVe5p3WiSlr"))
#             order = client.order.create({'amount': amt, 'currency': 'INR', 'payment_capture': '1'})
#             dt={'response_code':200,'comments':'payment preview by razorpay',"status":True} 
#             return Response(dt)
#         else:
#             print('yes you cod')
#             dt={'response_code':200,'comments':'payment preview code',"status":False} 
#             return Response(dt)
# #isme kam krna hai
# class SucccessPaymentRazorpay(ViewSet):
#     def create(self,request):
#         user_email=request.data.get('user_email')
#         time_slot = request.data.get('time_slot')
#         payment_mode = request.data.get('payment_mode')
#         address = request.data.get('address')
#         razorpay_payment_id=request.data.get('razorpay_payment_id')
#         razorpay_order_id=request.data.get('razorpay_order_id')
#         razorpay_signature=request.data.get('razorpay_signature')
#         if user_email=='' or payment_mode=='' or address=='':
#             dt={'response_code':200,'comments':'all fields required',"status":False} 
#             return Response(dt)
#         try:
#             print('cccccccccccccccc')
#             user_inst=User.objects.get(username=user_email)
#             print('user_inst',user_inst)
#             cart_featch = UserCart.objects.filter(user=user_inst,cart_status=False)
#             print('cart_featch',cart_featch)
#             total_pay = 0
#             store_user = ''
#             for x in cart_featch:
#                 total_pay = total_pay + x.final_price
#                 store_user = x.store_user
            
#             # a=request.data
#             # data={'razorpay_payment_id':razorpay_payment_id,'razorpay_order_id':razorpay_order_id,'razorpay_signature':razorpay_signature}
#             # datas={}
#             # for key ,val in data.items():
#             #     if key == 'razorpay_order_id':
#             #         datas['razorpay_order_id'] = val
#             #     elif key == 'razorpay_payment_id':
#             #         datas['razorpay_payment_id'] = val
#             #     elif key == 'razorpay_signature' :
#             #         datas['razorpay_signature'] = val
#             # print('ye data hai...',datas)
#             # data={}
#             client = razorpay.Client(auth=("rzp_test_oh9NnzT3WLdH8D", "2cVCx2C2jgbv9YVe5p3WiSlr"))
#             # check = client.utility.verify_payment_signature(datas)
#             # if check:
#             #     pass
#             # else:
            
#             try:

#                 address_inst = Delivery_address.objects.filter(user=user_inst).get(address=address)
#                 print('payment_mode',payment_mode)
#                 print(address_inst)
#                 # if time_slot:
#                 order_save = Order_detail(user=user_inst,payment_mode=payment_mode,payment_id=razorpay_payment_id,
#                                             order_id=razorpay_order_id,signature=razorpay_signature,
#                                             price=total_pay,store_user=store_user,time_slot=time_slot,delivery_address=address_inst,
#                                             order_mode='Self_Picking')
#                 order_save.save()
#             except:
#                 dt={'response_code':200,'comments':'no delivery address',"status":False} 
#                 return Response(dt)

#             # else:
#             #     print('condition run here...')
#             #     order_save = Order_detail(user=user_inst, payment_mode=payment_mode,
#             #                                 payment_id=datas['razorpay_payment_id'],
#             #                                 order_id=datas['razorpay_order_id'], signature=datas['razorpay_signature'],
#             #                                 price=total_pay, store_user=store_user,
#             #                                 delivery_address=address_inst,order_mode='Delivery')
#             #     order_save.save()
#             # order_save.item.set(cart_featch)
#             for x in cart_featch:
#                 x.cart_status = True
#                 x.save()
#             dt={'response_code':200,'comments':'payment successful',"status":True} 
#             return Response(dt)
#         except:
#             dt={'response_code':200,'comments':'user is not register',"status":False} 
#             return Response(dt)




# class PaymentByCod(ViewSet):
#     def create(self,request):
#         user_email=request.data.get('user_email')
#         time_slot = request.data.get('time_slot')
#         payment_mode = request.data.get('payment_mode')
#         address = request.data.get('address')
#         user_instance=User.objects.get(username=user_email)
#         cart_featch = UserCart.objects.filter(user=user_instance, cart_status=False)
#         total_pay = 0
#         store_user = ''
#         for x in cart_featch:
#             total_pay = total_pay + x.final_price
#             store_user = x.store_user
        
#         address_inst = Delivery_address.objects.filter(user=user_instance).get(address=address)
#         order_id = 'Cod_order'+ str(randint(1111,4444))
#         if time_slot:
#             print('code time slot mae hai..')
#             order_save = Order_detail(user=user_instance, payment_mode=payment_mode,
#                                         price=total_pay, store_user=store_user, time_slot=time_slot,
#                                         delivery_address=address_inst,order_mode='Self_Picking')
#             order_save.save()
#             obj=order_id+str(order_save.id)
#             order_save.order_id=obj
#             order_save.save()
#         else:
#             print('without time slot mae hai..')
#             print('condition run here...')
#             print('payment_mode',payment_mode)
#             order_save = Order_detail(user=user_instance, payment_mode=payment_mode,
#                                         price=total_pay, store_user=store_user,
#                                         delivery_address=address_inst,order_mode='Delivery')
#             order_save.save()
#             obj = order_id + str(order_save.id)
#             order_save.order_id = obj
#             order_save.save()

#         order_save.item.set(cart_featch)
#         for x in cart_featch:
#             x.cart_status = True
#             x.save()
#         dt={'response_code':200,'comments':'payment successful',"status":True} 
#         return Response(dt)

######ye update ho gya server pe

class OrderDetailByUser(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:

            user_inst=User.objects.get(username=user_email)
            try:
                order_query=Order_detail.objects.filter(user=user_inst)
                data_dict={}
                data_list=[]
                for x in order_query:
                    data_dict={'order_id':x.id,'user_id':x.user.id,'user_email':x.user.username,'store_user':x.store_user.store_name,'store_address':x.store_user.store_address,
                    'price':x.price,'order_status':x.order_status,'order_onpynt_id':x.order_id,'payment_mode':x.payment_mode,'order_date_time':x.date_time}
                    data_list.append(data_dict)
                dt={'order_details':data_list,'response_code':200,'comments':'orders details',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no order details',"status":False} 
                return Response(dt)

        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

class OrderCancel(ViewSet):
    def create(self,request):
            order_id = request.data.get('order_id')
            order_status=request.data.get('order_status')
            try:
                order_cacel_featch = Order_detail.objects.get(id=order_id )
                order_cacel_featch.order_status=order_status
                x=datetime.datetime.now()
                date_time=x.strftime("%a") + ' ' + x.strftime("%d") + ',' + x.strftime("%Y") + ',' + x.strftime(
                    "%I") + ':' + x.strftime("%M") + ' ' + x.strftime("%p")
                order_cacel_featch.cancel_date=date_time
                order_cacel_featch.save()
                dt={'response_code':200,'comments':'order is cancle',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no order id',"status":False} 
                return Response(dt)


class ShowRatingDetailsVariant(ViewSet):
    def create(self,request):
        varint_id=request.data.get('varint_id')
        if varint_id=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            variant_qur=Variants.objects.get(id=varint_id)
            like_data=LikesModelVariant.objects.filter(variants__id=varint_id).order_by('-id')
            avgs_rating=LikesModelVariant.objects.filter(variants__id=varint_id).aggregate(average_rating=Avg('rating')).get('average_rating')
            cout_rating=LikesModelVariant.objects.filter(variants__id=varint_id).aggregate(count_rating=Count('rating')).get('count_rating') 
            data_list=[]
            data_dict={}
            like_data=LikesModelVariant.objects.filter(variants__id=varint_id).order_by('-id')
            if like_data or avgs_rating or cout_rating:
                for x in like_data:
                    data_dict={'id':x.id,'user_email':x.user.username,'comments':x.comments,'likes':x.likes,'rating':x.rating}
                    data_list.append(data_dict)
                dt={'avgs_rating':avgs_rating,'cout_rating':cout_rating,'likes_details':data_list,'response_code':200,'comments':'avrage_rating and number of count rating',"status":True} 
                return Response(dt)
            else:
                dt={'avgs_rating':'no rating','cout_rating':'no count','likes_details':'no details','response_code':200,'comments':'no avrage_rating and number of count rating and details ',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'no Variants id ',"status":False} 
            return Response(dt)

class  CreateRatingDetailsVariant(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        varint_id=request.data.get('varint_id')
        comments=request.data.get('comments')
        likes=request.data.get('likes')
        rating=request.data.get('rating')
        if user_email=='' or varint_id=='' or comments=='' or likes=='' or rating=='':
            dt={'response_code':200,'comments':'all fields required ',"status":False} 
            return Response(dt)
        try:
            user_instance=User.objects.get(username=user_email)
            try:
                varint_instance=Variants.objects.get(id=varint_id)
                like_objet=LikesModelVariant(user=user_instance,variants=varint_instance,comments=comments,likes=likes,rating=rating)
                like_objet.save()
                dt={'response_code':200,'comments':'ceate likes models ',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no varint id ',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)
class DeleteRatingDetailVarint(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        rating_id=request.data.get('rating_id')
        if user_email=='' or rating_id=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_instn=User.objects.get(username=user_email)
            try:
                likesmdelobj=LikesModelVariant.objects.filter(user=user_instn).get(id=rating_id)
                likesmdelobj.delete()
                dt={'response_code':200,'comments':'delete comeent',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'model is not exit',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)











class ShowRatingDetailShop(ViewSet):
    def create(self,request):
        shop_id=request.data.get('shop_id')
        if shop_id=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            variants=Vendor_Store_detail.objects.get(id=shop_id)
            like_data=LikesModelShop.objects.filter(shop__id=shop_id).order_by('-id')
            avgs_rating=LikesModelShop.objects.filter(shop__id=shop_id).aggregate(average_rating=Avg('rating')).get('average_rating')
            cout_rating=LikesModelShop.objects.filter(shop__id=shop_id).aggregate(count_rating=Count('rating')).get('count_rating') 
            data_list=[]
            data_dict={}
            like_data=LikesModelShop.objects.filter(shop__id=shop_id).order_by('-id')
            if like_data or avgs_rating or cout_rating:
                for x in like_data:
                    data_dict={'id':x.id,'user_email':x.user.username,'comments':x.comments,'rating':x.rating}
                    data_list.append(data_dict)
                dt={'avgs_rating':avgs_rating,'cout_rating':cout_rating,'likes_details':data_list,'response_code':200,'comments':'avrage_rating and number of count rating',"status":True} 
                return Response(dt)
            else:
                dt={'avgs_rating':'no rating','cout_rating':'no count','likes_details':'no details','response_code':200,'comments':'no avrage_rating and number of count rating and details ',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'no Variants id ',"status":False} 
            return Response(dt)


class  CreateRatingDetailShop(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        shop_id=request.data.get('shop_id')
        comments=request.data.get('comments')
        rating=request.data.get('rating')
        if user_email=='' or shop_id=='' or comments==''  or rating=='':
            dt={'response_code':200,'comments':'all fields required ',"status":False} 
            return Response(dt)
        try:
            user_instance=User.objects.get(username=user_email)
            try:
                shop_instance=Vendor_Store_detail.objects.get(id=shop_id)
                like_objet=LikesModelShop(user=user_instance,shop=shop_instance,comments=comments,rating=rating)
                like_objet.save()
                dt={'response_code':200,'comments':'ceate likes models ',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no shop id ',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)
#################Refer_code shop##############
class DeleteRatingDetailShop(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        rating_id=request.data.get('rating_id')
        if user_email=='' or rating_id=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                likesmodel_obj=LikesModelShop.objects.filter(user=user_inst).get(id=rating_id)
                likesmodel_obj.delete()
                dt={'response_code':200,'comments':'delete likes models ',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no rating model ',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

class ReferIdStoreCreate(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        refer_code=request.data.get('refer_code')
        position=request.data.get('position')
        if user_email=='' or refer_code=='' or position=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            referobjet=Refer_id_store(user=user_inst,refer_code=refer_code,position=position)
            referobjet.save()

            dt={'response_code':200,'comments':'refer code create',"status":True} 
            return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)
class ReferIdStoreUpdate(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        refrmodle_id=request.data.get('refrmodle_id')
        refer_code=request.data.get('refer_code')
        position=request.data.get('position')
        if user_email=='' or refer_code=='' or position=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                referidstore=Refer_id_store.objects.filter(user=user_inst).get(id=refrmodle_id)
                referidstore.refer_code=refer_code
                referidstore.position=position
                referidstore.save()
                dt={'response_code':200,'comments':'refer code update',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no Refer_id_store modle id',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

class ReferIdStoreList(ViewSet):
    def list(self,request):
        referidstore_obj=Refer_id_store.objects.all()
        data_dict={}
        data_list=[]
        for x in referidstore_obj:
            data_dict={'user_id':x.user.id,'user_email':x.user.username,'referidstore_id':x.id,'referidstore_refer_code':x.refer_code,'referidstore_position':x.position,'referidstore_status':x.status,'date_time':x.date_time}
            data_list.append(data_dict)
        if data_list:
            dt={'referidstore_details':data_list,'response_code':200,'comments':'all list',"status":True} 
            return Response(dt)
        else:
            dt={'response_code':200,'comments':'no Refer_id_store',"status":False} 
            return Response(dt)

class ReferIdStoreListByUser(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                referidstore_obj=Refer_id_store.objects.filter(user=user_inst)
                data_dict={}
                data_list=[]
                for x in referidstore_obj:
                    data_dict={'user_id':x.user.id,'user_email':x.user.username,'referidstore_id':x.id,'referidstore_refer_code':x.refer_code,'referidstore_position':x.position,'referidstore_status':x.status,'date_time':x.date_time}
                    data_list.append(data_dict)
                dt={'referidstore_details':data_list,'response_code':200,'comments':'all list',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no Refer_id_store id',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

#######################################################################

class ReferCodeCreate(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        refercode=request.data.get('refercode')
        update_date_time=request.data.get('update_date_time')
        if user_email=='' or refercode=='':
            dt={'response_code':200,'comments':'all list',"status":True} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            refercode_obj=Refer_code(user=user_inst,refercode=refercode,update_date_time=update_date_time)
            refercode_obj.save()
            dt={'response_code':200,'comments':'refercode created',"status":True} 
            return Response(dt)
        except:
            dt={'response_code':200,'comments':'refercode created',"status":False} 
            return Response(dt)

class ReferCodeList(ViewSet):
    def list(self,request):
        refer_code_obj=Refer_code.objects.all()
        data_dict={}
        data_list=[]
        for x in refer_code_obj:
            data_dict={'user_id':x.user.id,'user_email':x.user.username,'refer_id':x.id,'refer_code':x.refercode,'update_date_time':x.update_date_time,'date_time':x.date_time}
            data_list.append(data_dict)
        if data_list:
            dt={'referidstore_details':data_list,'response_code':200,'comments':'all list',"status":True} 
            return Response(dt)
        else:
            dt={'response_code':200,'comments':'no Refer_code model ',"status":False} 
            return Response(dt)

class ReferCodeListByUser(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        if user_email=='':
            dt={'response_code':200,'comments':'all fields required ',"status":False} 
            return Response(dt)
        try:
            user_instance=User.objects.get(username=user_email)
            refer_code_obj=Refer_code.objects.filter(user=user_instance)
            data_dict={}
            data_list=[]
            for x in refer_code_obj:
                data_dict={'user_id':x.user.id,'user_email':x.user.username,'refer_id':x.id,'refer_code':x.refercode,'update_date_time':x.update_date_time,'date_time':x.date_time}
                data_list.append(data_dict)
            if data_list:
                dt={'referidstore_details':data_list,'response_code':200,'comments':'all list',"status":True} 
                return Response(dt)
            else:
                dt={'response_code':200,'comments':'no Refer_code model ',"status":False} 
                return Response(dt)  
        except:
            dt={'response_code':200,'comments':'user is not register ',"status":False} 
            return Response(dt)


class RandomAddress(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        address=request.data.get('address')
        if user_email=='' or address=='':
            dt={'response_code':200,'comments':'all fields required',"status":False} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
                add_lat_long = gmaps.geocode(address)
                user_lat = add_lat_long[0]['geometry']['location']['lat']
                user_lng = add_lat_long[0]['geometry']['location']['lng']
                # print('lat',user_lat)
                # print('log',user_lng)
                random_address_obj=random_address(user=user_inst,address=address,latitude=user_lat,longitude=user_lng)
                random_address_obj.save()
                dt={'response_code':200,'comments':'address created',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'address allready created',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

class RandomAddressUpdate(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        # random_add_id=request.data.get('random_add_id')
        address=request.data.get('address')
        if user_email=='' or address=='':
            dt={'response_code':200,'comments':'all field required',"status":True} 
            return Response(dt)
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                random_address_inst=random_address.objects.get(user=user_inst)
                random_address_inst.address=address
                gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
                add_lat_long = gmaps.geocode(address)
                user_lat = add_lat_long[0]['geometry']['location']['lat']
                user_lng = add_lat_long[0]['geometry']['location']['lng']
                random_address_inst.latitude=user_lat
                random_address_inst.longitude=user_lng
                random_address_inst.save()
                dt={'response_code':200,'comments':'address update',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no randum address model rcord',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)
        
class RandomAddressDelete(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        try:
            user_inst=User.objects.get(username=user_email)
            try:
                random_addr_inst=random_address.objects.get(user=user_inst)
                random_addr_inst.delete()
                dt={'response_code':200,'comments':'random address delete',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no random address model',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is register',"status":False} 
            return Response(dt)

###########################


class SelfPickingMode(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        order_mode = request.data.get('order_mode')
        time_slot = request.data.get('time_slot')
        refer = request.data.get('refer_code')
        position = request.data.get('position_value')
        payment_mode = request.data.get('payment_mode')
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        address = request.data.get('address')
        city = request.data.get('city')
        pincode = request.data.get('pincode')
        locality = request.data.get('locality')
        landmark = request.data.get('landmark')
        alternate_mobile = request.data.get('alternate_phone')
        try:
            user_instance=User.objects.get(username=user_email)
            try:
                cart_featch = UserCart.objects.filter(user=user_instance, cart_status=False)
                print('cart_featch',cart_featch)
                total_pay = 0
                store_user =''
                for x in cart_featch:
                    total_pay = total_pay + x.final_price
                    store_user=x.store_user
                from datetime import date
                import calendar
                my_date = date.today()
                obj = calendar.day_name[my_date.weekday()]
                try:
                    slot_featch = vendor_time_slot.objects.filter(vendor_store=store_user, day=obj)
                    print(slot_featch, 'ye slot featch hai..')
                    if order_mode == 'Self_Picking':
                        if refer:
                            try:
                                refer_featch = Refer_code.objects.get(refercode=refer)
                                try:
                                    refer_store_featch = Refer_id_store.objects.get(user=user_instance)
                                except:
                                    refer_store_table = Refer_id_store(user=user_instance,refer_code=refer,position=position,)
                                    refer_store_table.save()
                            except:
                                from datetime import date
                                import calendar
                                my_date = date.today()
                                obj = calendar.day_name[my_date.weekday()]
                                slot_featch = vendor_time_slot.objects.filter(vendor_store=store_user, day=obj)
                                dt={'response_code':200,'comments':'Invalid Refer Code Please provide valid refer code..',"status":True} 
                                return Response(dt)
                        if time_slot and payment_mode:
                            if payment_mode=='Wallet':
                                pass
                            elif payment_mode =='Razorpay':
                                amt = int(total_pay * 100)
                                print(amt)
                                print('run....')
                                client = razorpay.Client(auth=("rzp_test_oh9NnzT3WLdH8D", "2cVCx2C2jgbv9YVe5p3WiSlr"))
                                order = client.order.create({'amount': amt, 'currency': 'INR', 'payment_capture': '1'})
                                user_details={'user_email':user_email,'order_mode':order_mode,'time_slot':time_slot,'refer_code':refer,'position_value':position,'payment_mode':payment_mode,'name':name,'phone':phone,'email':email,'address':address,'city':city,'pincode':pincode,'locality':locality,'landmark':landmark,'alternate_phone':alternate_mobile}
                                dt={'user_details':user_details,'response_code':200,'comments':'Razorpay payment done',"status":True} 
                                return Response(dt)
                            elif payment_mode == 'COD':
                                dt={'response_code':200,'comments':'COD paymnet ',"status":True} 
                                return Response(dt)
                    elif order_mode == 'By_Delivery':
                        if address:
                            print('code run here')
                            gmaps = googlemaps.Client(key='AIzaSyC5m-C32piW2yiT3kevVbvLfHXsLsPTWik')
                            add_lat_long = gmaps.geocode(address)
                            user_lat = add_lat_long[0]['geometry']['location']['lat']
                            user_lng = add_lat_long[0]['geometry']['location']['lng']
                            newport_ri = (user_lat, user_lng)
                            cleveland_oh = (store_user.store_latitude, store_user.store_longitude)
                            c = geodesic(newport_ri, cleveland_oh).miles
                            km = c / 0.62137
                            if km <= 10:
                                if refer:
                                    print('condition yha tk chla')
                                    try:
                                        refer_featch = Refer_code.objects.get(refercode=refer)
                                        try:
                                            refer_store_featch = Refer_id_store.objects.get(user=user_instance)
                                        except:
                                            refer_store_table = Refer_id_store(user=user_instance, refer_code=refer,
                                                                                position=position, )
                                            refer_store_table.save()
                                    except:
                                        print('ab yha chla')
                                        dt={'response_code':200,'comments':'Invalid Refer Code Please provide valid refer code..',"status":True} 
                                        return Response(dt)
                                if payment_mode:
                                    if payment_mode == 'Wallet':
                                        pass
                                    elif payment_mode == 'Razorpay':
                                        amt = int(total_pay * 100)
                                        print(amt)
                                        print('run....')
                                        client = razorpay.Client(auth=("rzp_test_oh9NnzT3WLdH8D", "2cVCx2C2jgbv9YVe5p3WiSlr"))
                                        order = client.order.create({'amount': amt, 'currency': 'INR', 'payment_capture': '1'})
                                        dt={'response_code':200,'comments':'Razorpay payment done',"status":True} 
                                        return Response(dt)
                                    elif payment_mode=='COD':
                                        dt={'response_code':200,'comments':'COD payment done',"status":True} 
                                        return Response(dt)
                            else:
                                dt={'response_code':200,'comments':'Delivery are not available to your provided area',"status":True} 
                                return Response(dt)
                        else:
                            dt={'response_code':200,'comments':'not deliver on this address',"status":True} 
                            return Response(dt)
                    else:
                        dt={'response_code':200,'comments':'select currect order_mode',"status":False} 
                        return Response(dt)
                except:
                    dt={'response_code':200,'comments':'no vandor time slot ',"status":False} 
                    return Response(dt)
            except:
                dt={'response_code':200,'comments':'no user card',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not regiater',"status":False} 
            return Response(dt)

    







class SucccessPaymentRazorpayNew(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        time_slot = request.data.get('time_slot')
        payment_mode =request.data.get('payment_mode')
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        address = request.data.get('address')
        city = request.data.get('city')
        pincode = request.data.get('pincode')
        locality = request.data.get('locality')
        landmark = request.data.get('landmark')
        alternate_mobile = request.data.get('alternate_phone')
        order_mode = request.data.get('order_mode')
        razorpay_order_id=request.data.get('razorpay_order_id')
        razorpay_payment_id=request.data.get('razorpay_payment_id')
        razorpay_signature=request.data.get('razorpay_signature')
        try:
            user_instance=User.objects.get(username=user_email)
            try:
                cart_featch = UserCart.objects.filter(user=user_instance,cart_status=False)
                total_pay = 0
                store_user = ''
                for x in cart_featch:
                    total_pay = total_pay + x.final_price
                    store_user = x.store_user
                datas={'razorpay_order_id':razorpay_order_id,'razorpay_payment_id':razorpay_payment_id,'razorpay_signature':razorpay_signature}
                data={}
                for key ,val in datas.items():
                    if key == 'razorpay_order_id':
                        data['razorpay_order_id'] = val
                    elif key == 'razorpay_payment_id':
                        data['razorpay_payment_id'] = val
                    elif key == 'razorpay_signature' :
                        data['razorpay_signature'] = val
                print('ye data hai...',data)
                client = razorpay.Client(auth=("rzp_test_oh9NnzT3WLdH8D", "2cVCx2C2jgbv9YVe5p3WiSlr"))
                try:
                    check = client.utility.verify_payment_signature(data)
                    pass
                except:
                    print('payment_mode',payment_mode)
                    # print(address_inst)
                    if order_mode=='Self_Picking':
                        order_save = Order_detail(user=user_instance,payment_mode=payment_mode,payment_id=data['razorpay_payment_id'],
                                                    order_id=data['razorpay_order_id'],signature=data['razorpay_signature'],
                                                    price=total_pay,store_user=store_user,time_slot=time_slot,
                                                    order_mode='Self_Picking')
                        order_save.save()
                    elif order_mode=='By_Delivery':
                        deli_address = Delivery_address(user=user_instance, full_name=name,
                                                            phone=phone, email=email, address=address, city=city,
                                                            pincode=pincode,
                                                            locality=locality, landmark=landmark,
                                                            alternate_mobile=alternate_mobile)
                        deli_address.save()
                        order_save = Order_detail(user=user_instance, payment_mode=payment_mode,
                                                    payment_id=data['razorpay_payment_id'],
                                                    order_id=data['razorpay_order_id'], signature=data['razorpay_signature'],
                                                    price=total_pay, store_user=store_user,
                                                    delivery_address=deli_address,order_mode='By_Delivery')
                        order_save.save()
                    else:
                        dt={'response_code':200,'comments':'not valid order model',"status":False} 
                        return Response(dt)
                    #order_save.item.set(cart_featch)
                    for x in cart_featch:
                        prod_fake = Product_fake(Buyer=user_instance,stor_details=x.store_user,category=x.variant_id.product.category,subcategory=x.variant_id.product.subcategory,
                                            brand_name=x.variant_id.product.brand_name,title=x.variant_id.product.title,price=x.variant_id.product.price,
                                            discount_percent=x.variant_id.product.discount_percent,gst_percent=x.variant_id.product.gst_percent,variant=x.variant_id.product.variant,
                                            image=x.variant_id.product.image)
                        prod_fake.save()
                        var_fake = Variants_fake(title=x.variant_id.title,real_var_id=x.variant_id.id,product=prod_fake,color=x.variant_id.color,size=x.variant_id.size,description=x.variant_id.description,
                                                    image_fornt=x.variant_id.image_fornt,image_back=x.variant_id.image_back,image_side=x.variant_id.image_side,
                                                    quantity=x.quantity,price=x.variant_id.price,point_value=x.variant_id.point_value,after_discount_price=x.variant_id.after_discount_price,
                                                    variant_discount=x.variant_id.variant_discount)
                        var_fake.save()
                        order_save.item.add(var_fake)
                        var_featch=Variants.objects.get(id=x.variant_id.id)
                        var_featch.quantity=var_featch.quantity-x.quantity
                        var_featch.save()
                        # x.cart_status = True
                        # x.save()
                    cart_featch.delete()
                    dt={'response_code':200,'comments':'SucccessPaymentRazorpayNew',"status":True} 
                    return Response(dt)
            except:
                dt={'response_code':200,'comments':'no usercart',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not registr',"status":False} 
            return Response(dt)




################################# End Success Payment / Razorpay #############
class PaymentByCod(ViewSet):
    def create(self,request):
        user_email=request.data.get('user_email')
        time_slot = request.data.get('time_slot')
        payment_mode = request.data.get('payment_mode')
        name = request.data.get('name')
        phone = request.data.get('phone')
        email = request.data.get('email')
        address = request.data.get('address')
        city = request.data.get('city')
        pincode = request.data.get('pincode')
        locality = request.data.get('locality')
        landmark = request.data.get('landmark')
        alternate_mobile = request.data.get('alternate_phone')
        order_mode = request.data.get('order_mode')
        try:
            user_instance=User.objects.get(username=user_email)
            try:
                cart_featch = UserCart.objects.filter(user=user_instance, cart_status=False)
                total_pay = 0
                store_user = ''
                for x in cart_featch:
                    total_pay = total_pay + x.final_price
                    store_user = x.store_user
                order_id = 'Cod_order'+ str(randint(1111,4444))
                if order_mode=="Self_Picking":
                    order_save = Order_detail(user=user_instance, payment_mode=payment_mode,
                                                price=total_pay, store_user=store_user, time_slot=time_slot,
                                                order_mode='Self_Picking')
                    order_save.save()
                    obj=order_id+str(order_save.id)
                    order_save.order_id=obj
                    order_save.save()
                elif order_mode=='By_Delivery':
                    deli_address = Delivery_address(user=user_instance, full_name=name,
                                                    phone=phone, email=email, address=address, city=city,
                                                    pincode=pincode,
                                                    locality=locality, landmark=landmark,
                                                    alternate_mobile=alternate_mobile)
                    deli_address.save()
                    order_save = Order_detail(user=user_instance, payment_mode=payment_mode,
                                                price=total_pay, store_user=store_user,
                                                delivery_address=deli_address,order_mode=order_mode)
                    order_save.save()
                    obj = order_id + str(order_save.id)
                    order_save.order_id = obj
                    order_save.save()
                else:
                    dt={'response_code':200,'comments':'not valid order mode',"status":False} 
                    return Response(dt)
                for x in cart_featch:
                    prod_fake = Product_fake(Buyer=user_instance, stor_details=x.store_user,
                                                category=x.variant_id.product.category,
                                                subcategory=x.variant_id.product.subcategory,
                                                brand_name=x.variant_id.product.brand_name, title=x.variant_id.product.title,
                                                price=x.variant_id.product.price,
                                                discount_percent=x.variant_id.product.discount_percent,
                                                gst_percent=x.variant_id.product.gst_percent,
                                                variant=x.variant_id.product.variant,
                                                image=x.variant_id.product.image)
                    prod_fake.save()
                    var_fake = Variants_fake(title=x.variant_id.title, product=prod_fake, color=x.variant_id.color,
                                                real_var_id=x.variant_id.id,size=x.variant_id.size, description=x.variant_id.description,
                                                image_fornt=x.variant_id.image_fornt, image_back=x.variant_id.image_back,
                                                image_side=x.variant_id.image_side,
                                                quantity=x.quantity, price=x.variant_id.price,
                                                point_value=x.variant_id.point_value,
                                                after_discount_price=x.variant_id.after_discount_price,
                                                variant_discount=x.variant_id.variant_discount)
                    var_fake.save()
                    order_save.item.add(var_fake)
                    var_featch = Variants.objects.get(id=x.variant_id.id)
                    var_featch.quantity = var_featch.quantity - x.quantity
                    var_featch.save()
                    # x.cart_status = True
                    # x.save()
                cart_featch.delete()
                dt={'response_code':200,'comments':'pyament success',"status":True} 
                return Response(dt)
            except:
                dt={'response_code':200,'comments':'no usercart',"status":False} 
                return Response(dt)
        except:
            dt={'response_code':200,'comments':'user is not register',"status":False} 
            return Response(dt)

   

##################################################################



































