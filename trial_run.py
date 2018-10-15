# -*- coding: utf-8 -*-
key = ''

while True:
    try:
        alpha = input('Please enter a value for alpha between 0 and 1:')
        alpha = float(alpha)
        if alpha > 0 and alpha < 1:
            print("Your choice is %.2f" % alpha)
           
            
            
            
        else:
            print("Your input is out of range. Please try again")
        
        
    except:
        print("Invalid entry, please try again: ")
       