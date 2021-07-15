def repeater(string, n):
    arr = string
    while(n != 1):
        arr = arr + string
        n = n - 1
        
    return arr
