"""
    Write a function that returns the longest contiguous palindromic substring in s. 
    In the event that there are multiple longest palindromic substrings, return the 
    first to occur.
"""


def longest_palindrome(s):
    if is_palindrome(s):
        return s
    max_pal = ''
    for i in range(len(s)):
        temp = check(i, i, s)
        if len(max_pal) < len(temp):
            max_pal = temp
    return max_pal


def check(li, ri, s):
    if li > 0 and ri < len(s):
        if is_palindrome(s[li - 1:ri + 2]):
            return check(li - 1, ri + 1, s)
        elif is_palindrome(s[li:ri + 2]):
            return check(li, ri + 1, s)
        elif is_palindrome(s[li - 1:ri + 1]):
            return check(li - 1, ri, s)
    return s[li:ri + 1]


def is_palindrome(s):
    return s == s[::-1]
