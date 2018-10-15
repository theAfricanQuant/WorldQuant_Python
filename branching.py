# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 21:12:56 2018

LAB: Branching Program

@author: Ricky Macharm
World Quant University
WQU 605 Programming in Python I
"""

import function_test as ft

name = 'Hello Ricky'
fuel_cost = 6          #cost of fuel per unit currency (eg US$)
work_distance = 27     #one-way distance to work (eg km)
fuel_level = 3.0    #amount of fuel currently in the tank (eg litre)
consumption_rate = 14  #distance per unit of fuel (eg 14 km/litre)

trip_cost = ft.calc_price(work_distance,fuel_cost,consumption_rate)

print("The cost of fuel for the present trip is: US$ %.2f" % trip_cost)

threshold = work_distance / consumption_rate  #amount of fuel for a journey


 # print(threshold)

low = 'You will not make it to work without refueling first!'
exact = 'You have just enough fuel to get to work, but \ will not make it home'
some_extra = 'You will need to refuel in the near \ future...'
surplus = 'You have plenty of fuel, have a safe drive \ to work today!'


if fuel_level < threshold:
    print(low)
    
elif fuel_level == threshold:
    print(exact)
    
elif fuel_level > threshold and  fuel_level < threshold + 1:
    print(some_extra)
        
else:
    print(surplus)

