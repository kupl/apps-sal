import math


def is_palindrome(string):
    new_string = str(string)
    last_element = len(new_string) - 1
    half_arra = math.floor(len(new_string) / 2)
    for item in range(0, half_arra):
        if new_string[item] != new_string[last_element]:
            return False
        last_element = last_element - 1
    return True
