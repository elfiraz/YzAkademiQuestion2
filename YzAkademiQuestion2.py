# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:27:44 2022

@author: asus
"""

def time (hour, minute): 
    nums = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen", 
            "seventeen", "eighteen", "nineteen", 
            "twenty", "twenty one", "twenty two", 
            "twenty three", "twenty four", 
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]; 
    if hour  <= 23 and minute  <= 59 :
        if (minute == 0): 
            print("It's",nums[hour], "o'clock"); 
  
        elif (minute == 15): 
            print("It's quarter past", nums[hour],"o'clock"); 
  
        elif (minute == 30):
            print("It's half past", nums[hour],"o'clock"); 
  
        elif (minute == 45): 
            print("It's quarter to", (nums[(hour % 12) + 1]),"o'clock"); 
  
        elif ( 1 <= minute <= 30): 
            print("It's",nums[minute],"minutes past", nums[hour],"o'clock"); 
  
        elif (30 <= minute <=59): 
            print("It's",nums[60 - minute], "minutes to", nums[(hour % 12) + 1],"o'clock"); 
    else: 
        print('invalid format') 

  
 
h = int(input('Please enter hours = ')); 
m = int(input('Please enter minute = ')); 
time (h, m);