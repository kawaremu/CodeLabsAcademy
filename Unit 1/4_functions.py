import math

# Write a Python function that checks whether a passed string is palindrome or not. 
# A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def palindrome(word:str) -> bool:
  return word[::] == word[::-1]



# Write a Python function that takes a number as a parameter and checks if the number is prime or not. 
# A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
def is_prime(number:int) -> bool:
  for i in range(2,number):
    if number % i == 0:
      return False
  return True


# Write a Python function to check whether a number is in a given range.
def is_in_range(number,range) -> bool:
  return number in range

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# 5! = 1x2x3x4x5
def factorial_rec(number:int) -> int:
  if number == 0:
    return 1
  else:
    return factorial_rec(number-1)*number
  
def factorial(number:int) -> int:
  if number == 0:
    return 1
  else:
    fact = 1
    for i in range(1,number+1):
      fact =fact*i
    return fact


# Write a Python program to reverse a string.
def reverse(string:str) -> str:
  return string[::-1]

# Write a Python function to sum all the numbers in a list.
def sum_numbers(input_list:list) -> int:
  sum = 0
  for element in input_list:
    sum += element
  return sum

# Write a Python function to find the Max of three numbers.

def max_of_three(a,b,c):
  if a > b and a > c:
    return a  
  if b > a and b > c:
    return b  
  return c
  
  

print(max_of_three(10, 14, 500))