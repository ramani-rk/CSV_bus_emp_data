from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

import csv
def insert_emp_data(self):
    with open ('C:\\Users\\Ezhilkanthan\\OneDrive\\Desktop\\django projects\\django\\Scripts\\project40i\\app\\Business-employment-data-september-2022-quarter-csv.csv', 'r') as FO:
        IDO=csv.reader(FO)
        next(IDO)
        for id in IDO:
            sr=id[0]
            pr=id[1]
            dv=id[2]
            sd=id[3]
            st=id[4]
            ut=id[5]
            mt=id[6]
            st=id[7]
            gp=id[8]
            st1=id[9]
            st2=id[10]
            st3=id[11]
            st4=id[12]
            st5=id[13]

            ERO = Business_emp_data(Series_reference=sr,Period=pr,Data_value=dv,Suppressed=sd,STATUS=st,UNITS=ut,Magnitude=mt,Subject=st,Group=gp,Series_title_1=st1,Series_title_2=st2,Series_title_3=st3)
            ERO.save()
    return HttpResponse ('Business Employee Data is Inserted Successfully!!!!!')