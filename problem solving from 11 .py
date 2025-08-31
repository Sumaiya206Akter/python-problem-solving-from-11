
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

#------------------problem 13-------------------
# Q-- Write a Python program that takes a year as input and determines if it is a leap year or not.
input_year = int(input("input year:"))# get input from user
def leap_year_checker(): # create a function to check if input year leap year or not
    if input_year %4 == 0 and not input_year %100 == 0:# used conditon if input year is not divisible by 100 but divisible by 4 then it is a leap year
        print(f"{input_year} is leapyear")# if above condition met print it is a leap year
    elif input_year %100 == 0 and input_year %400 == 0: # used condition if input year is divisible by 100 and also divisible by 400 then it is a leap year 
        print(f"{input_year} is a leap year")# if condition met print this line 
    else:
        print(f"{input_year} is not a leap year")# if above two condition are not satisfied than print this line
leap_year_checker()

#------------------problem 14-------------------
# Q--Write a Python program that takes a student’s percentage as input and prints their corresponding grade according to the following criteria: – 90% or above: A+ – 80-89%: A – 70-79%: B – 60-69%: C – Below 60%: Fail
bangla_result = int(input("what percentage of marks did you achieve in your bangla exam ?:"))# get achived mark from student
english_result = int(input("what percentage of marks did you achieve in english exam ?:"))# get achived mark from student
math_result = int(input("what percentage of marks did you achieve in your math exam ?:"))# get achived mark from student
science_result = int(input("what percentage of marks did you achieve in your science exam ?:"))# get achived mark from student
bgs_result = int(input("what percentage of marks did you achieve in your bgs exam ?:"))# get achived mark from student
religion_result = int(input("what percentage of marks did you achieve in your religion exam ?:"))# get achived mark from student
group_subject1 = int(input("what percentage of marks did you achieve in your group subject exam(physics/Accounting/History) ?:"))# get achived mark from student
group_subject2 = int(input("what percentage of marks did you achieve in the exam(chemistry/Business Entrepreneurship/Civics) ?:"))# get achived mark from student
group_subject3 = int(input("what percentage of marks did you achieve in the exam(biology/Finance & Banking/Geography)?:"))# get achived mark from student
group_subject4 = int(input("what percentage of marks did you achieve in the exam(higher math/ Business Organization & Management/Economics)?:"))# get achived mark from student
optional_subject = int(input("input your optional subject marks:"))
all_mark = [bangla_result, english_result, math_result, science_result, bgs_result, religion_result, group_subject1, group_subject2, group_subject3, group_subject4, optional_subject]# list all resust 
all_gpa = []# list all gpa 
def grade_calculator():# create a functhin to calculate grade
    for x in all_mark:# create a loop to calculate gpa from all_mark list
        if x >= 80:# if x is greater than is equale 80
            all_gpa.append(5.00)# add point ina all_gpa list
        elif x >= 70:# if x is greater than is equale 70
            all_gpa.append(4.00)# add point ina all_gpa list
        elif x >= 60:# if x is greater than is equale 60
            all_gpa.append(3.50)# add point ina all_gpa list
        elif x >= 50:# if x is greater than is equale 50
            all_gpa.append(3.00)# add point ina all_gpa list
        elif x >= 40:# if x is greater than is equale 40
            all_gpa.append(2.00)# add point ina all_gpa list
        elif x >=33 and x < 40:# if x is greater than equal 33 or less than equal 40
            all_gpa.append(1.00)# add point ina all_gpa list
        else:
            all_gpa.append(0.00)# otherwise print this line
    if 0.00 in all_gpa:# if all_gpa list have this line"you are failed" than print this line below . 
        print("your gpa or grade is 0")
    sum_gpa = sum(all_gpa) - all_gpa[-1] # sum all point and than remore optional subjects point
    if all_gpa[-1] > 2.00:
        addable_optionalgpa = all_gpa[-1]- 2.00 # substraction 2 from optional subjects mark
    else:
        addable_optionalgpa = all_gpa[-1]
    gpa_without_optional_subject = sum_gpa/9 # divide total gpa with total subject without optional subject
    average_gpa = gpa_without_optional_subject + addable_optionalgpa # add optional subject gpa and this is the final gpa
    if average_gpa >=5.00: # if average gpa is greater than 5 than print  below line
        print("your gpa is 5.00")
    else:
        print(f"your gpa is {average_gpa}")# if average gpa less than 5 print current gpa
    # condition for calculate grade 
    if average_gpa >= 5: 
        print("your grade is 5.00")
    elif average_gpa >= 4:
        print("your grade is A")
    elif average_gpa >= 3.50:
        print("your grade is A-")
    elif average_gpa >= 3:
            print("your grade is B")
    elif average_gpa >= 2:
        print("your grade is C")
    elif average_gpa >= 1:
        print("your grade is D")
    else:
        print("your grade is F. you are failed . please get up and try your best next time")
        
grade_calculator() # print average grade 

#----------------------------problem 14---------------------