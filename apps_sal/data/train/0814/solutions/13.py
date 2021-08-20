from collections import defaultdict
for t in range(int(input())):
    n = int(input())
    store = list(map(int, input().split()))
    count = 0
    curr = 0
    cStore = defaultdict()
    for i in range(n):
        if store[i] == 0:
            if curr > 0:
                curr += 1
            else:
                curr = 1
        elif curr != 0:
            if curr in cStore:
                cStore[curr] += 1
            else:
                cStore[curr] = 1
            curr = 0
    flag = 0
    maxi = 0
    for val in cStore:
        if cStore[val] > 1:
            flag = 1
            break
        elif val > maxi:
            maxi = val
    if flag == 1:
        print('No')
    elif maxi % 2 == 0:
        print('No')
    else:
        print('Yes')
