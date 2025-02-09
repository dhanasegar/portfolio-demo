# from django.db import models
# from django.contrib.auth.models import User
# from django.template.defaultfilters import slugify
# from ckeditor.fields import RichTextField



# class Skill(models.Model):
#     class Meta:
#         verbose_name_plural = 'Skills'
#         verbose_name = 'Skill'
    
#     name = models.CharField(max_length=100, blank=True, null=True)
#     score = models.IntegerField(default=80, blank=True, null=True)
#     is_key_skill = models.BooleanField(default=False)
    
#     def __str__(self):
        
#         return self.name

# class UserProfile(models.Model):
#     class Meta:
#         verbose_name_plural = 'User Profiles'
#         verbose_name = 'User Profile'

#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
#     title = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)
#     skills = models.ManyToManyField(Skill, blank=True)
#     cv = models.FileField(upload_to='resumes/', null=True, blank=True)  
#     cv_binary = models.BinaryField(null=True, blank=True)  

#     def save(self, *args, **kwargs):
#         if self.cv and not self.cv_binary:  
#             self.cv_binary = self.cv.read()  
#             self.cv.close()  
#         super(UserProfile, self).save(*args, **kwargs)  



# class ContactProfile(models.Model):
    
#     class Meta:
#         verbose_name_plural = 'Contact Profiles'
#         verbose_name = 'Contact Profile'
#         ordering = ["timestamp"]
#     timestamp = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(verbose_name="Name",max_length=100)
#     email = models.EmailField(verbose_name="Email")
#     message = models.TextField(verbose_name="Message")

#     def __str__(self):
#         return f'{self.name}'
# from django.db import models

# class Testimonial(models.Model):

#     class Meta:
#         verbose_name_plural = 'Testimonials'
#         verbose_name = 'Testimonial'
#         ordering = ["id"]

#     thumbnail = models.ImageField(blank=True, null=True, upload_to="testimonials")
#     name = models.CharField(max_length=200, blank=True, null=True)
#     role = models.CharField(max_length=200, blank=True, null=True)
#     quote = models.CharField(max_length=500, blank=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name


# class Media(models.Model):

#     class Meta:
#         verbose_name_plural = 'Media Files'
#         verbose_name = 'Media'
#         ordering = ["name"]
	
#     image = models.ImageField(blank=True, null=True, upload_to="media")
#     url = models.URLField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     is_image = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if self.url:
#             self.is_image = False
#         super(Media, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.name

# class Portfolio(models.Model):

#     class Meta:
#         verbose_name_plural = 'Portfolio Profiles'
#         verbose_name = 'Portfolio'
#         ordering = ["name"]
#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     slug = models.SlugField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Portfolio, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/portfolio/{self.slug}"


# class Blog(models.Model):

#     class Meta:
#         verbose_name_plural = 'Blog Profiles'
#         verbose_name = 'Blog'
#         ordering = ["timestamp"]

#     timestamp = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=200, blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     slug = models.SlugField(null=True, blank=True)
#     # image = models.ImageField(blank=True, null=True, upload_to="blog")
#     is_active = models.BooleanField(default=True)

#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.name)
#         super(Blog, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return f"/blog/{self.slug}"


# class Certificate(models.Model):

#     class Meta:
#         verbose_name_plural = 'Certificates'
#         verbose_name = 'Certificate'

#     date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=50, blank=True, null=True)
#     title = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

# class Resume(models.Model):
#     name = models.CharField(max_length=255)  # For descriptive purposes
#     file = models.BinaryField()  # To store the file in binary format
#     uploaded_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(max_length=500, blank=True, null=True)  # Increased max_length for flexibility
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)
    cv_binary = models.BinaryField(null=True, blank=True)  # Retained for potential use

    def save(self, *args, **kwargs):
        if self.cv and not self.cv_binary:
            with self.cv.open('rb') as file:
                self.cv_binary = file.read()
        super(UserProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username if self.user else "Unlinked Profile"



class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["id"]

    thumbnail = models.URLField(blank=True, null=True)  # Thumbnail field as URL
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.URLField(blank=True, null=True)  # Image field as URL
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)  # Portfolio image as URL
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)  # Blog image as URL
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Resume(models.Model):
    name = models.CharField(max_length=255)
    file = models.BinaryField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

