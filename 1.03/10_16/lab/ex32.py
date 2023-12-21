# 1a) Write a Python function to find the maximum of three numbers
# NOTE: do not utilize built-in functions to accomplish this
# instead, opt for conditionals
...


# 1b) use this function to find the max of the 3 vars below
a = float("inf")
b = float("-inf")
c = 100000000
print(max(a, b, c))


# 2a) Write a Python program to reverse a string
def reverse_string(string):
    return string[::-1]


# 2b) Use this function to reverse the string saved in the name below
word = "racecar"

print(reverse_string(word))


# 3a) Write a Python function to multiply all the numbers in a list.
def multiply_nums(num_list):
    answer = 1
    for num in num_list:
        answer = answer * num
    return answer


# 3b) Use this function to find the product of the list below
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(multiply_nums(nums))


# 4a) Write a Python function that finds the maximum value of a list
# NOTE: do not use built-in Python functions. Instead use a for-loop and
# a conditional
def find_max(num_list):
    max_num = float("-inf")
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

# 4b) Use this function to find the product of the list below
nums = [100, 491, 592, 58, 3, 59, -100]
print(find_max(nums))
