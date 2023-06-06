"""
Created on Sun Apr 29 20:05:56 2018

@author: Ricky Macharm
World Quant University
WQU 605 Programming in Python I
"""

import random

# function definitions
def do_exp(choice, numb=5, pwr=2, rt=2):
    def random_square():
        ans = random.randrange(100)
        ans **= 2
        return ans

    def user_power(num, power):
        x = num ** power
        print("Here's %d to the power of %d: %d" %(num, power, x))

    def user_root(num, root = 2):
        x = num **(1/root)
        print("Here's %d to the inverse power of %d: %d" %(num, root, x))

    if choice == 1:
        return random_square()
    elif choice == 2:
        return user_power(numb, pwr)
    else:
        return user_root(numb, rt)


def calc_price(dist, fuel_cost, rate):
    """ This function will calculate the cost of a trip based on a distance inputed by the user.
    fuel_cost is the cost of fuel per unit, dist is the estimated distance to be covered during the trip,
    rate is the consumption rate of the vehicle to be used"""
    return fuel_cost * (dist / rate)  # cost of fuel for a journey