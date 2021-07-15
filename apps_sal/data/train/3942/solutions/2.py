def solve(n, cnt=0):    
    if n%10: return -1
    for i in (500,200,100,50,20,10):
        cnt += n//i
        n = n%i
    return cnt
