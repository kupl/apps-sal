
from sys import stdin
import sys

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = stdin.readline()
    a = a[:-1]

    zero = []
    one  = []
    ans  = []

    for i in a:
        if i == "0":
            if len(zero) == 0:
                zero.append(len(zero)+len(one)+1)
            ans.append(zero[-1])
            one.append(zero[-1])
            del zero[-1]
        else:
            if len(one) == 0:
                one.append(len(zero)+len(one)+1)
            ans.append(one[-1])
            zero.append(one[-1])
            del one[-1]

    print(len(zero) + len(one))
    print(*ans)
            

    

