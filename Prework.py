#Question 1
def hello_name(user_name):
     print(f'Hello {user_name}!')

#Question 2
def first_odds():
    for x in range(100):
        if x % 2 == 1:
            print(x)
            
#Question 3
def max_num_in_list(a_list):
    return max(a_list)

#Question 4
def is_leap_year(a_year):
    return(a_year % 400 == 0 or a_year % 100 != 0 and a_year % 4 == 0)

#Question 5
def is_consecutive(a_list):
    for x in range(len(a_list) - 1):
        if a_list[x+1] - a_list[x] != 1:
            return False
    return True