import re


def longest_palindrome(s):
    s = list(re.sub('[\\W_]+', '', s.lower()))
    solution = 0
    j = 0
    letter_count = 0
    for letter in s:
        letter_count = s.count(letter)
        if letter_count % 2 == 0:
            solution += letter_count
        else:
            solution += letter_count - 1
            j = 1
        s = [i for i in s if i != letter]
    return solution + j
