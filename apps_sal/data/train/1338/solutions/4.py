import math
s = input().split()
for i in range(1,2*int(s[0])+1,2):
    a = float(s[i])
    b = float(s[i+1])
    res = a*pow(10,b)
    print('{:.2f}'.format(res))

