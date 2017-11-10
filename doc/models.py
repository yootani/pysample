# models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here


# Create Table 'Document'
class Document(models.Model):
	title	= models.CharField(max_length=100)
	body	= models.CharField(max_length=1000)

	# User and Document's Reration by the 'UserViewDocument'
	user_view_document = models.ManyToManyField(User, through='UserViewDocument')

# Create View 'UserViewDocument'
class UserViewDocument(models.Model):
	user 	= models.ForeignKey(User)
	document= models.ForeignKey(Document)


