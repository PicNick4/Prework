#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
     print(f'Hello {user_name}!')

#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range(100):
        if x % 2 == 1:
            print(x)
            
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    return max(a_list)

#Question 4
#Write a function to return if the given year is a leap year.
def is_leap_year(a_year):
    return(a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 == 0)

#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers.
def is_consecutive(a_list):
    for x in range(len(a_list) - 1):
        if a_list[x+1] - a_list[x] != 1:
            return False
    return True