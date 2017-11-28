# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:42:56 2017

@author: stusdent
"""

import xlsxwriter

class Employee:
   

   def __init__(self, fname, lname, dob,city):
      self.fname = fname
      self.lname = lname
      self.dob = dob
      self.city = city
      
my_emp = []

for i in range(1,10):
    fname=input("Enter Fname:")
    lname=input("Enter Lname:")
    dob=input("Enter dd/mm/yy:")
    city=input("Enter city:")
    
    my_emp.append(Employee(fname, lname, dob,city))     

workbook = xlsxwriter.Workbook('file.xlsx')
worksheet = workbook.add_worksheet()


worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 20)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 20)


bold = workbook.add_format({'bold': True})


worksheet.write('A1', 'First Name',bold)

worksheet.write('B1', 'Last Name', bold)
worksheet.write('C1', 'DOB', bold)
worksheet.write('D1', 'City', bold)

for i in range(1,10):
       worksheet.write(i, 0, my_emp[i].fname)
       worksheet.write(i, 1,  my_emp[i].lname)
       worksheet.write(i, 2,  my_emp[i].dob)
       worksheet.write(i, 3,  my_emp[i].city)
       i=i+1
       



workbook.close()