# -*- coding: utf-8 -*-

import unittest
from emp import Employee

class Testemp(unittest.TestCase):
    
    
    
    def test_yearlysalary(self):
        empt1 = Employee('TESTER1','LA',13,300,41)
        self.assertEqual(empt1.yearly_salary(),3600)
        empt2 = Employee('TESTER1','LA',13,0,32)
        with self.assertRaises(ValueError): #context manager: can be used for testing exceptions
            empt2.yearly_salary()
        
    def test_fullname(self):
        empt1 = Employee('TESTER1','LA',13,300,41)
        empt2 = Employee('TESTER2','LA',13,2000,32)
        self.assertEqual(empt1.full_name, 'TESTER1 LA')
        self.assertEqual(empt2.full_name, 'TESTER2 LA')
        
    def test_email(self):
        empt1 = Employee('TESTER1','LA',13,300,41)
        empt2 = Employee('TESTER2','LA',13,2000,32)
        self.assertEqual(empt1.email_add, 'TESTER1LA@sap.com')
        self.assertEqual(empt2.email_add, 'TESTER2LA@sap.com')
        
        

if __name__ == '__main__':
    unittest.main()

