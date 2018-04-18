# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=100) #标题
	category = models.CharField(max_length=50, blank=True) #标签
	datetime = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		ordering = ['-datetime']
