def find_lowest_int(k):
    n=2
    while True:
        if sorted(str(n*k))==sorted(str(n*(k+1))):return n
        n+=1
