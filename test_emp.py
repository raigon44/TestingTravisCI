# -*- coding: utf-8 -*-

import unittest
from emp import Employee

class Testemp(unittest.TestCase):
    
    
    
    def test_yearlysalary(self):
        empt1 = Employee('TESTER1','LA',13,300,41)
        self.assertEqual(empt1.yearly_salary(),3600)
        

if __name__ == '__main__':
    unittest.main()

