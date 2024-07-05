from django.db import models


class IE(models.Model):
    job_role=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    Domain=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)
    
    
class WE(models.Model):
    job_role=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    Domain=models.CharField(max_length=100)
    Duration=models.CharField(max_length=100)
    
    
class MP(models.Model):
    project_name=models.CharField(max_length=100)
    key_skills=models.CharField(max_length=100)
    project_url=models.CharField(max_length=300)
    
    
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.BigIntegerField()
    message=models.TextField(max_length=1000)
    