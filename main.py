# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 00:35:32 2017

@author: Colmos
"""

#!/usr/bin/python
import re

from event import event
   
def main():  
   
   print "****************************************************"
   print "*                  Event Locator                   *"
   print "****************************************************\n"
   choice = raw_input("Please enter coordinates (x,y):")
   
   matches = re.match("^([-+]?[0-9]|[-+]?10),([-+]?[0-9]|[-+]?10)$", choice)
   
   while (matches == None):
       print "Input error - coordinates must be in the range of -10 to 10 and comma seperated! e.g. 5,5"
       choice = raw_input("Please enter coordinates (x,y):")
       matches = re.match("^([-+]?[0-9]|[-+]?10),([-+]?[0-9]|[-+]?10)$", choice)
          
   #if matches:
        #Do the rest of the search etc
               
       
   
   
   
main()