def index(array, n):
    ans = 1
    if n > len(array)-1:
        return -1
    else:
        for i in range (n):
           ans *= array[n] 
        return ans
