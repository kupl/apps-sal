"""
This is a tricky problem

as we can remove some substrings and there are only two characters the maximum
possible answer is 2
1. Remove all a
2. Remove all b

"""


def is_palindrome(s):
    result = True
    for i in range(len(s)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True


testcase = int(input())
for z in range(testcase):
    s = input()
    if is_palindrome(s):
        print(1)
    else:
        print(2)
