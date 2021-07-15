def max_multiple(d, b):
    #your code here
    for n in range(b+1,d,-1):
        if n%d == 0 and n <= b:
            return n

