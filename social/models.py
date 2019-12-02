from django.db import models
from django.contrib.auth.models import User

# validators=[RegexValidators("^0?[5-9]{1}\d(9)$")],
class Profile(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField('Profile', on_delete=models.CASCADE)
    age = models.IntegerField(default=18)#validators=[MinValueValidator(18)]
    phone = models.CharField( max_length=15 , null=True, blank=True)
    status = models.CharField(max_length=100,default='single', choices=(('single','single'),('married','married'),('widow','widow')))
    gender = models.CharField(max_length=100,default='female', choices=(('male','Male'),('female','Female')))
    description = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    pic = models.ImageField(upload_to="profile/", null=True)

class Post(models.Model):
	pic = models.ImageField(upload_to="post_images/", null=True)
	subject = models.TextField(null=True,blank=True)
	message = models.TextField(null=True,blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	uploaded_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
	def __str__(self):
		self.subject

class PostComment(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	message = models.TextField(null=True,blank=True)
	comment_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	flag = models.CharField(max_length=100,choices=(('racist','racist'),('abusive','abusive'),('pornography','pornography')))
	def __str__(self):
		self.post[:20]

class PostLike(models.Model):
	post = models.ForeignKey('Post', on_delete=models.CASCADE)
	liked_by = models.ForeignKey('Profile', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		self.liked_by

class PostFollow(models.Model):
	profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	followed_by = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='followed_by')
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		self.followed_by