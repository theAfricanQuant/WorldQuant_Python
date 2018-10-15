# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:22:14 2018

@author: Ricky Macharm
"""

import math

def square(x):
    ans = x**2
    return ans
    

def get_simple_interest():
    p = float(input("Enter a decimal value for the principal: "))
    r = float(input("Enter a decimal value for the interest rate: "))
    t = int(input("Enter the duration of the loan: "))
    try:
        i = p*r*t
    except ValueError:
        print("Incorrect values entered, program exiting")
        return  #this line simply causes the function to exit
    return i
    

def compound_interest(p, r, t):
    #A = Pe^(rt)
    #where: P = principal, r=rate, t=time
    result = p * math.exp(r * t)
    return result 


def get_car_payment():
    try:
        loan = float(input("Enter the value of the loan: "))
        down_payment = float(input("Enter a down payment,use 0 if no money down: "))
        rate = float(input("Enter the decimal value of interest rate: "))
        dur = int(input("Enter the number of months for the term: "))
        if (loan*down_payment*rate*dur) < 0:
            print("Negative number detected! Program exiting")
            return
    except ValueError:
        print("Invalid characters entered, restarting program")
        get_car_payment()
    def calculate(l,down,apr,duration):
        apr = apr/12
        principal = (l-down)
        i = principal * apr
        apr = apr+1
        combined_rate = apr**duration
        inv = 1/combined_rate
        final = 1 - inv
        payment = i/final
        return payment
    monthly = calculate(loan,down_payment,rate,dur)
    
    print("**Your monthly payment will be %.2f" % monthly)
    