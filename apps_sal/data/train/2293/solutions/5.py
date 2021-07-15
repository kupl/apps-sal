def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [None]*(2**n)
    d[0] = [a[0], 0, -1, -1]
    ans = 0
    for i, t1 in enumerate(a[1:]):
        i += 1
        t2, t3, t4 = i, -1, -1
        for j in range(len(bin(i))-2):
            k = i & ~(1 << j)
            if k == i:
                continue
            t5, t6, t7, t8 = d[k]
            if t5 > t1:
                t1, t2, t3, t4 = t5, t6, t1, t2
            elif t5 > t3:
                if t6 != t2:
                    t3, t4 = t5, t6
            if t7 > t3:
                t3, t4 = t7, t8
        d[i] = [t1, t2, t3, t4]
        ans = max(ans, t1+t3)
        print(ans)


main()
