tri = lambda x: (x * (x+1))/2

def sum_triangular_numbers(n):
    try:
        res = 0
        for i in range(1,n+1):
            res += tri(i)
        return res
    except: return 0

