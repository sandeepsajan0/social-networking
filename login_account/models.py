# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length = 100, default ='')
	city = models.CharField(max_length = 100,default ='')
	website = models.URLField(default='')
	phone = models.IntegerField(default= 0)
	
# Create your models here.
def create_profile(sender, **kargs):
	if kargs['created']:
		user_profile= UserProfile.objects.create(user = kargs['instance'])

post_save.connect(create_profile,sender = User)
