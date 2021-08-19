def getInvCount(arr):
    inv_count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inv_count += 1
    return inv_count


q = int(input())
for i in range(q):
    n = int(input())
    s = input()
    t = input()
    if set(s) != set(t):
        print('NO')
        continue
    if len(set(s)) < len(s):
        print('YES')
        continue
    elif len(s) <= 26 and getInvCount(list(s)) % 2 == getInvCount(list(t)) % 2:
        print('YES')
    else:
        print('NO')
