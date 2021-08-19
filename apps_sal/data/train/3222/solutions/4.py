# Beginner Sum of Numbers by Dr. Professor, Esq.
#
# input:     any two numbers, positive or negative, as a and b
# output:    print the sum all numbers between a and b; including a and b
#
# pseudo-code:
# test for equality
#    if equal print a
#
# if a greater than b
#    loop through the value of each number between b and a
#    accumulate each value in x
#
# if b greater than a
#    loop through the value of each number between a and b
#    accumulate each value in x
#
# return x

def get_sum(a, b):
    x = 0
    if a == b:
        return a

    elif a > b:
        for i in range(b, a + 1):
            x += i
    elif b > a:
        for i in range(a, b + 1):
            x += i
    return x
