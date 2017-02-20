# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 11:50:56 2016

@author: ryo
"""
class Men:
    def __init__(self,name):
        self.name = name
        print("Initialized!")
        
    def hello(self):
        print("Hello " + self.name +"!")
        
    def goodbye(self):
        print("Good-bye " + self.name + "!")
        
m = Men("David")
m.hello()
m.goodbye()