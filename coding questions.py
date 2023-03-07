#question 1
def hello_name(user_name):
    print(f"Hello, {user_name}")
hello_name("John")

#question 2
def first_odds():
    for num in range(1, 101):
        if num % 2 == 1:
            print(num)

#question 3
def max_num_in_list(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

#question 4
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False
    
#question 5
def consecuctive_numbers(num_list):
    n = len(num_list)
    if n < 2:
        return True
    else:
        for i in range(1, n):
            if num_list[i] != num_list[i - 1]+1:
                return False
        return True
