def count_sixes(n):
    num = 3*2**(n-1)
    c=0
    if n%2 ==0 and int(str(num)[:2]) < 15:
        c = 1
    elif n%2 == 1 and int(str(num)[0]) < 3:
        c=1
    return len(str(num))-1 -c
