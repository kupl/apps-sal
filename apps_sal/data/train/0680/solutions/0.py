t = int(input())
(l, r, x) = (0, 0, 0)
ans = []
for i in range(t):
    (n, m) = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    suma = sum(a)
    sumb = sum(b)
    q = int(input())
    for j in range(q):
        l1 = list(map(int, input().split()))
        if l1[0] == 1:
            l = l1[1]
            r = l1[2]
            x = l1[3]
            suma = suma + (r - l + 1) * x
        elif l1[0] == 2:
            l = l1[1]
            r = l1[2]
            x = l1[3]
            sumb = sumb + (r - l + 1) * x
        else:
            ans.append(suma * sumb % 998244353)
for i in range(len(ans)):
    print(ans[i])
