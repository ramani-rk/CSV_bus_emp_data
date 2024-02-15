from django.db import models

# Create your models here.

class Business_emp_data(models.Model):
    Series_reference = models.CharField(max_length=100)
    Period=models.FloatField()
    Data_value=models.CharField(max_length=50)
    Suppressed=models.CharField(max_length=50,null=True)
    STATUS=models.CharField(max_length=100)
    UNITS=models.CharField(max_length=50)
    Magnitude=models.IntegerField()
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=200)
    Series_title_2=models.CharField(max_length=200)
    Series_title_3=models.CharField(max_length=200)



    def __str__ (self):
        return self.Series_reference
