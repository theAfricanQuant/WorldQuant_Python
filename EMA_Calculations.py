# -*- coding: utf-8 -*-
import Calc_EMA as ce
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

 
invalidFileName = True
while invalidFileName:
    
    try:
        invalidFileName = False
        fileName = input("Input the correct name of file and extension:  ") 
        infile = open(fileName, 'r')
        
    except FileNotFoundError as e1:
        print('an error occured while opening the file. Check file name and file location then try again')
        print(e1)
        invalidFileName = True
    except Exception as e2:
        print('Sorry an error occured')
        print(e2) 
        invalidFileName = True
    else:   
        
        s1 = infile.readline()
        s2 = infile.readline()
       
        infile.close()

s1 = s1.rstrip('\n')
s2 = s2.rstrip('\n')

s1 = s1.split(',')
s2 = s2.split(',')


s1 = s1[1:len(s1)]
s2 = s2[1:len(s2)]


Time_Period = []
for x in range(0,len(s1)):
    Time_Period.append(int(s1[x]))
    
Value = []
for x in range(0,len(s2)):
    Value.append(float(s2[x]))
    
Time_Period1 = []
for x in range(0,(len(s1)+1)):
    Time_Period1.append(x+1)
    
    
run_again = True
while run_again:
    try:
        run_again = False
        alpha = input('Please enter a value for alpha between 0 and 1:')
        alpha = float(alpha)
        ema = []
        if alpha > 0 and alpha < 1:
            print("Your choice is %.2f" % alpha)
            ema = ce.ExponentialMovingAverage(alpha, Value)
            
            print(Time_Period)
            print(Time_Period1)
            print(Value)
            print(ema)
            
        else:
            
            print('Invalid entry. Please try again')
            run_again = True
            
    except:
        print("Invalid entry. Please try again: ")
        run_again = True
        
    else:
        # plotting the points 
            plt.plot(Time_Period, Value)

            plt.plot(Time_Period1, ema)

            # naming the x axis
            plt.xlabel('Time Period')
            # naming the y axis
            plt.ylabel('Values')

            # giving a title to my graph
            plt.title('Value and EMA Smoothing')

            # function to show the plot
            plt.show()
            
            #plt.pause(0.01)
           
            
            # Loop for call back
            incorrect = True
            while incorrect:
                incorrect = False
                print('Do you wish to test another value of alpha?')
                ans = input("Input 'Y' or 'N': ")
                                  
                if ans.upper()== 'Y':
                    run_again = True
                elif ans.upper() == 'N':
                    print("Thank you for your time.")
                    break
                                
                else:
                    print('Please, check your entry and try again')
                    incorrect = True
                        
            




x = np.array(Time_Period)
y = np.array(Value)
gradient, intercept, r_value, p_value, std_err = stats.linregress(x,y)
mn=np.min(x)
mx=np.max(x)
x1=np.linspace(mn,mx,500)
y1=gradient*x1+intercept
plt.plot(x,y, 'ob')
plt.plot(x1,y1, '-r')
plt.show()