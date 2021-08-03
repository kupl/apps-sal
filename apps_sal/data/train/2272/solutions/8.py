def main():
    from bisect import bisect_right as br
    import numpy as np
    n = int(input())
    a = np.array(list(map(int, input().split())))
    b = np.array(list(map(int, input().split())))
    #n = 100000
    #a = np.array([i+1 for i in range(n)])
    #b = np.array([2*i+2 for i in range(n)])
    a = np.sort(a)
    b = np.sort(b[::-1])
    m = n % 2
    xor = 0
    for i in b:
        xor ^= i
    b = pow(2, 28) - b
    ans = 0
    for loop in range(28, -1, -1):
        j = pow(2, loop)
        k = (xor & j) // j
        temp = br(b, j - 1)
        b[temp:] -= j
        b = np.sort(b)
        temp = br(a, j - 1)
        k += sum((a & j) // j)
        a[temp:] -= j
        x = (k + br(b, 0)) * m % 2
        a = np.sort(a)
        x += np.sum(np.searchsorted(b, a + 1))
        ans += (x % 2) * j
    print(ans)


main()
