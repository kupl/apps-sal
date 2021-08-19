# cook your dish here
try:
    n = int(input())
    n += 1
    flag = 1
    while n <= 987654321:
        nt = str(n)
        if "0" not in nt:
            if len(nt) == len(set(list(nt))):
                print(n)
                flag = 0
                break
            n += 1
        else:
            nt = nt[::-1]
            ind = nt.index('0')
            n += 10**ind
    if flag:
        print(0)
except:
    pass
