
for _ in range(int(input())):
    a = input()
    i = 0
    j = len(a) - 1
    ans = 1
    mod = (10**7) + 9
    while i <= j:
        if a[i] == '?' and a[j] == "?":
            ans = ((ans % mod) * (26 % mod)) % mod
            i += 1
            j -= 1
        elif a[i] == '?' or a[j] == "?" or a[i] == a[j]:
            i += 1
            j -= 1
        else:
            ans = 0
            break
    print(ans)
