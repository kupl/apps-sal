def find_longest(arr):
    counter = 0
    number = 0
    for n in arr:
        str_n = str(n)
        if len(str_n) > counter:
            counter = len(str_n)
            number = n
    return number 
