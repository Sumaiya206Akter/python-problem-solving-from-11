
#--------------------problem 11---------------
#Q--Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.
input_number= int(input("write a number:"))# get number input from user 
if input_number > 0 :# used a conditon - if the inputed number is greater than 0
    print(f"{input_number} is a positive number ") # if the condition is met this will be printed
elif input_number < 0: # used a condition -if the inputed number is less than 0
    print(f"{input_number} is a negative number")# if the condition is met this will be printed 
else:
    print(f"{input_number} . this number is zero") # if above 2 conditon doesn't met than this will be printed

#------------------------problem 12----------------------
#Q-- Write a Python program that takes three numbers as input and prints the largest among them.

number1 = int(input("input 1st number:"))# get 1st input from user and change type str to int 
number2 = int(input("input 2nd number:"))# get 2nd input from user and change type str to int 
number3 = int(input("input 3rd number:"))# get 3rd input from user and change type str to int 
number_list = [number1, number2, number3]# a list with 3 input

# procedure 1 - using max()
largest1 = max(number_list)# use mex() method to find largest number and keep it in this variable 
print(f"the largest number is {largest1} from the number_list [procedure 1]")# print the largest number

#procedure 2 use loop
largest2 = number_list[0] # keep 1st list item in largest variable
for number in number_list: # use for loop
    if number > largest2: # used condition if number greater than largest number 
        largest2 = number # if the number is greater than current largest value than update the largest value to the number
print(f"the largest number is {largest2}") # print final largest number

#procedure 3 use reduce() 
from functools import reduce # import reduce function from the functools module
largest3 = reduce(lambda x , y : x if x > y else y, number_list)# used lambda function in reduce function to compare x, y in the list a and return largest value
print(largest3, "is the largest number")

#procedure 4 use sort()
number_list.sort() # use sort() method to ascending order
print(number_list[-1] , " is the largest number ")# since the list is sorted in ascending order , the last value is the largest number

#----------------------problem 13---------------------

