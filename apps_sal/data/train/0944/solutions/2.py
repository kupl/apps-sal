# cook your dish here
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    odd, even, pref = [0], [0], [0]
    d = dict()

    ans = 0

    for i in range(n):
        if arr[i] & 1:
            odd.append(odd[-1] + 1)
            even.append(even[-1])
        else:
            odd.append(odd[-1])
            even.append(even[-1] + 1)
        pref.append(pref[-1] + arr[i])
        if arr[i] in d:

            if arr[i] & 1:
                if abs(odd[i + 1] - odd[d[arr[i]]] - 2) & 1:
                    ans = max(ans, pref[i + 1] - pref[d[arr[i]]] - 2 * arr[i])
            else:
                if abs(even[i + 1] - even[d[arr[i]]] - 2) % 2 == 0:
                    ans = max(ans, pref[i + 1] - pref[d[arr[i]]] - 2 * arr[i])
        d[arr[i]] = i
    print(ans)
