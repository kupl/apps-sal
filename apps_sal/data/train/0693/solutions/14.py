#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

#Read the number of test cases.
import math
def facto(n):
    return math.factorial(n)
    
t=int(input())
while t:
    t = t - 1
    n=int(input())
    print(facto(n))

