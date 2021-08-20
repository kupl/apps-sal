n = int(input())
for i in range(n):
    (k, l) = map(int, input().split())
    bc = l
    ans = 0
    kp = 1000000007
    for j in range(1, k + 1):
        bc = pow(l, 2 * j - 1, kp)
        ans = (bc + ans) % kp
        l = l * bc % kp
    print(ans)
'511620149'
