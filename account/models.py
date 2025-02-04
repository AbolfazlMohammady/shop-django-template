from django.db import models
from django.contrib.auth.models import User

# Create your models here
# class Profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     melicode=models.CharField(max_length=10)
#     fathers_name=models.CharField(max_length=20)
#     image=models.ImageField(upload_to='profiles/images',blank=True)
#     def __str__(self):
#         return self.user.username
#     def save(self, *args, **kwargs):
#             self.melicode=self.melicode.replace('-','')
#             super(Profile,self).save(args,kwargs)
#     class Meta:
#         verbose_name_plural='حساب های کاربری'
#         verbose_name= 'حساب کاربری'
