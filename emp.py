# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 12:43:08 2018

@author: I323327
"""
#import configparser
#import os

class Employee:
    def __init__(self,fname,lname,age,pay,grade):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.pay = pay
        self.grade = grade
        self.employee_dir = "Employess"
        
        
        #if not os.path.exists(self.employee_dir):
            #os.makedirs(self.employee_dir)
            
        
        #self.config = configparser.RawConfigParser()
        #self.config.read('model.properties')

    @property
    def full_name(self):
        return(self.fname + ' ' + self.lname)
    
        
    @property   
    def email_add(self):
        return(self.fname + self.lname + '@' + 'sap.com')
        
    
    
    def yearly_salary(self):
        if self.pay == 0:
            raise ValueError('Salary cannot be zero !!!')
        yslry = self.pay * 12
        return yslry
        

if __name__ == '__main__':
    print("this is the main program")
    print("this line of code cannot be executeed when called from another program")

emp1 = Employee('Raigon','Augustin',25,1000,3)
emp2 = Employee('Test','user',28,2000,23)


#print(emp1)
#print(emp2)


print(emp2.yearly_salary())
print(emp1.email_add)