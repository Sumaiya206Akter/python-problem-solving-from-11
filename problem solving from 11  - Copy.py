
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

# ------------------------Problem-15 ----------------------
# Q---Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.
input_letter = input("enter a letter to check if it is a vowel or consonant:").lower()
#get letter input from user and transfer it to lower case if it is uppercase
vowel = ["a", "e" , "i" , "o" , "u"]# list of vowel
if len(input_letter) == 1:# find the lenght 
    if input_letter.isalpha():#check only letter
        if input_letter in vowel:# if entired letter is in aeiou
            print(f"{input_letter} is a vowel")# if condition satisfied than print this line
        else: 
            print(f"{input_letter} this is not a vowel")# if entired letter is not in the vowel list than print it
    else:
        print("please don't input number or special character")# if entired input is not a letter than print this line
else:# if the input_letter is not only one character or n
    print("write only one character.")
    
# ---------------------problem 16------------------------
# Q--- Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.
from datetime import datetime, time # import datetime and time function from datetime 
import pytz # import pytz for providing the necessary tools to perform acurate and reliable time zone calculation 
current_datetime = datetime.now(pytz.timezone("Asia/Dhaka")) # get curretnt date time 
print(current_datetime.strftime("%X %x")) # print current date and time
current_time = current_datetime.time() # get current time

if current_time >= time(4, 0) and current_time < time(12,0): # if the time is 4 am to 12 pm than print good morning
    print('Good morning')
elif current_time >= time(12, 0) and current_time < time(18,0):# if the time is 12pm to 6 pm than pirnt good afternoon
    print('Good Afternoon')
elif current_time >= time(18, 0): # if the time is greter than 6  pm 
    print("Good evening")# than condition satisfied print good evening 
    bedtime = input("are your going to bed?(Yes/no)").lower() # ask whether he/she is going to sleep ?
    if bedtime == "yes":# if it is bedtime than print good night
        print("ok good night. Have a nice sleep")
    else:
        print("ok.do you like to have a coffee together?")
#-----------------------------problem 17----------------------
#Q--Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle
try:
    side1 = float(input("input first side of your tringle:"))# get first side of a tringle from user
    side2 = float(input("input second side of your tringle:"))# get second side of a tringle from user
    side3 = float(input("input third side of your tringle:"))# get third side of a tringle from user
    triangle = [side1, side2, side3] # list of 3 sides
    maxside = max(triangle) # find maximum side
    sum_of_others = side1 + side2 + side3 - maxside # sum of others sides without maximum side
    if sum_of_others > maxside: # check if triangle formation is possible 
        if side1 == side2 == side3:# if first side , seconde side and third side are equal than print this  following line
            print("this is an equilateral triangle")
        if side1 == side2 or side2 == side3 or side3 == side1:# any two sides are equal then this is an isosceles triangle and print this following line 
            print("this is an isosceles triangle")
        else: # if no sides are equal
            print(" this is an scalene triangle") # if no sides are equal than print this line
    else:
        print("not possible to make a triangle by using this sides")
except ValueError:# if user don't enter a vaied input than show a message 
    print("please enter a valid number")
    