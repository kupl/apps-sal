def memoize_sum_dif(f):
    memory = {}
    
    def inner(n):
        if n not in memory:
            memory[n] = f(n)
        return memory[n]
    return inner
    
    
@memoize_sum_dif
def sum_dif_rev(n):
    
    if n == 1: return 45
    
    num = sum_dif_rev(n-1)
    
    while True:
        num = num+1
        if str(num)[::-1][0] == "0" or abs(num - int(str(num)[::-1])) == 0 :
            continue
        if (num + int(str(num)[::-1]))%abs(num - int(str(num)[::-1])) == 0:
            break              
    return num
