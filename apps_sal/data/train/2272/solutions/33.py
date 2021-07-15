def main():
    from bisect import bisect_right as br
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    m = n % 2
    xor = 0
    for i in b:
        xor ^= i
    for i in range(n):
        b[i] = 2**28 - b[i]
    ans = 0
    for loop in range(28, -1, -1):
        j = pow(2, loop)
        k = (xor & j) // j
        temp = br(b, j-1)
        for i in range(temp, n):
            b[i] -= j
        b.sort()
        temp = br(a, j-1)
        for i in a[:temp]:
            k += (i & j) // j
        for i in range(temp, n):
            k += (a[i] & j) // j
            a[i] -= j
        x = (k+br(b, 0))*m % 2
        a.sort()
        l = 0
        for i in a:
            while l < n:
                if i >= b[l]:
                    l += 1
                else:
                    break
            x += l % 2
        ans += (x % 2)*j
    print(ans)


main()

