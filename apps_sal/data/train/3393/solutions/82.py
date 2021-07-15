def list_squared(m, n):
    # your code   
    import numpy as np
    # find the divisors all together with array operarions instead of for loop (TOO SLOW!)
    def find_divisor_square(n):
        arr = np.arange(1,n+1)
        arr = n/arr
        divs = arr[arr == arr.astype(int)]
        return divs**2
        
    res = []
    for num in range(m,n):
        divs = find_divisor_square(num)
        sum_squres = divs.sum()
        if (sum_squres**0.5).is_integer(): # checks whether a float obj is an integer
            res.append([num, sum_squres])
    return res

