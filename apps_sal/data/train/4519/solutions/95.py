def max_number(n):
    lst = [num for num in str(n)]
    lst.sort(reverse = True)
    return int(''.join(lst))
    #your code here

