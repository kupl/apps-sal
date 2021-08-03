# cook your dish here
# ecapr203

try:
    # if(True):
    for _ in range(int(input())):
        n = int(input())
        k = int((((9 + (8 * n))**(0.5)) - 1) / 2)
        m = ((k - 1) * (k + 2)) // 2
        d = n - m
        if(d == 0):
            print(k - 1)
        else:
            print(d - 1)
except:
    pass
