# Given an non-negative integer return a murmur: "1 sheep ... 2 sheep ... 3 sheep ..."
def count_sheep(n):
    sheepy = ""
    counter = 1
    while counter <= n:
        sheepy += str(counter) + " sheep..."
        counter += 1
    return sheepy

# Filter out strings in a list 
def filter_list(l):
    return [i for i in l if not isinstance(i, str)]

# Reverse a string
def solution(string):
    return string[::-1]

# If your name starts with "R," you're playing the banjo!
def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return (name + " plays banjo")
    else:
        return (name + " does not play banjo")

# Basic calculator
def basic_op(operator, value1, value2):
    result = 0
    if operator == "+":
        result = value1 + value2 
    elif operator == "-":
        result = value1 - value2 
    elif operator == "*":
        result = value1 * value2 
    elif operator == "/":
        result = value1 / value2 
    return result

# Can you find the needle in the haystack?
# Write a function that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle.
def find_needle(haystack):
    position = haystack.index("needle")
    for needle in haystack:
        if needle == "needle":
            return f"found the needle at position {position}"
        else:
            pass

# Find the shortest word in a list:
def find_short(s):
    shortest = min(s.split(), key = len)
    return len(shortest)

#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
def array_diff(a, b):
    c = [n for n in a if n not in b]
    return c

#Find the smallest number in a list
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]