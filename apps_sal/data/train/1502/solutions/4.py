from collections import Counter
for _ in range(int(input())):
    strs = set(input().strip())
    lens = int(input())
    inps = [x for x in input().split()]
    isOK = True
    for i in strs:
        if i not in inps:
            isOK = False
            break
    print(1 if isOK else 0)
