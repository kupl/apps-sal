from sys import stdin
from math import ceil


def func(arr):
    step = 0
    right = len(arr) - 1
    n = len(arr)
    while(right != 1):
        step += 1
        if n % 2 != 0:
            right -= (2**(step - 1))
        else:
            arr[0] -= arr[right]
        n = ceil((n - 1) / 2) + 1
    return arr[0]


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    f = int(stdin.readline())
    indexes = [i for i, x in enumerate(arr) if x <= f]
    if len(indexes) == 0:
        print("impossible")
    else:
        print("possible")
        final = {}
        for ele in indexes:
            part = arr[0:ele]
            p = len(part)
            part = part[0:p:2]
            if p % 2 != 0:
                part.append(0 - part[-1])
            else:
                part.append(0)
            case = arr[ele:] + part
            ans = [case[-1]] + case[0:len(case) - 1]
            m = abs(func(ans))
            if m in final:
                final[m].append(ele)
            else:
                final[m] = [ele]
        print(min(final[min(list(final.keys()))]) + 1, min(list(final.keys())) + f)
