'''
    Write a function that returns the longest contiguous palindromic substring in s. 
    In the event that there are multiple longest palindromic substrings, return the 
    first to occur.
'''
import re


def longest_palindrome(string):
    if len(string) < 2:
        return string
    string = '|' + '|'.join(string) + '|'
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2 * C - i
        if R > i:
            LPS[i] = min(R - i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))
    return string[c - r: c + r].replace("|", "")
