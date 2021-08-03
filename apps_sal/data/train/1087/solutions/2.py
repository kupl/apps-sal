def main():
    try:
        [n, m] = input().split()
        m = int(m)
        n = int(n)
        p = [0] * (n + 1)
        while m > 0:
            [a, b] = input().split()
            a = int(a)
            b = int(b)
            p[a] = p[a] + 1
            p[b] = p[b] + 1
            if (p[a] >= 3 or p[b] >= 3):
                print("NO")
                return 0
            m = m - 1
        print("YES")
    except:
        return 0


main()
