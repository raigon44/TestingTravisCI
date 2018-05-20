# -*- coding: utf-8 -*-

import unittest
from emp import Employee

class Testemp(unittest.TestCase):
    
    def setUp(self):
        self.empt1 = Employee('TESTER1','LA',13,300,41)
        self.empt2 = Employee('TESTER2','LA',13,0,32)
        
    def tearDown(self):
        print("tear down")
    
    
    def test_yearlysalary(self):
        
        self.assertEqual(self.empt1.yearly_salary(),3600)
        
        with self.assertRaises(ValueError): #context manager: can be used for testing exceptions
            self.empt2.yearly_salary()
        
    def test_fullname(self):

        self.assertEqual(self.empt1.full_name, 'TESTER1 LA')
        self.assertEqual(self.empt2.full_name, 'TESTER2 LA')
        
    def test_email(self):

        self.assertEqual(self.empt1.email_add, 'TESTER1LA@sap.com')
        self.assertEqual(self.empt2.email_add, 'TESTER2LA@sap.com')
        
        

if __name__ == '__main__':
    unittest.main()

