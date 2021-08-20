mod = 1000000007
t = int(input())
while t:
    (l, r) = list(map(int, input().split()))
    ans = 0
    if l == r:
        print(l % mod)
    else:
        temp = l
        i = 1
        j = 1
        while temp:
            if temp & 1:
                tp2 = l & i
                k = min(r - l + 1, i - tp2 + 1)
                ans = (ans + j * k) % mod
            i <<= 1
            i += 1
            j <<= 1
            temp >>= 1
        print(ans % mod)
    t -= 1
