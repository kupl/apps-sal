def square_sum(numbers):
    #your code here
    s = []                 #empty list to store the result from loop below
    for x in numbers:     #loop through argument value
        x = x**2         #square value and assign
        s.append(x)     #append new value to list s
    return sum(s)     #sum of list after loop finishes
