from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=50, choices=(
                                                ("IT", "IT"), 
                                                ("Finance", "Finance"), 
                                                ("Healthcare", "Healthcare")
                                                 ))
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name+'----'+self.location
    
class Employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    position=models.CharField(max_length=50, choices=(
                                                ("Manager", "Manager"), 
                                                ("Developer", "Developer"), 
                                                ("Analyst", "Analyst"),
                                                ("HR", "HR"),
                                                ("Sales", "Sales"),
                                                ("Support", "Support"),
                                                ("tester", "tester")
                                                 ) )
    added_date=models.DateTimeField(auto_now_add=True)