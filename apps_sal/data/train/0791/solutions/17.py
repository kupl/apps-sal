def main():
    t = eval(input())
    while t > 0:
        n, d = list(map(int, input().split()))
        l = list(map(int, input().split()))
        count = 0
        k = sum(l)
        if k % n != 0:
            print("-1")
        else:
            r = sum(l) / n
            for i in range(n - d):
                if l[i] < r:
                    count += r - l[i]
                    l[i + d] -= r - l[i]
                    l[i] = r
                else:
                    count += l[i] - r
                    l[i + d] += l[i] - r
                    l[i] = r
            if l.count(r) == n:
                print(count)
            else:
                print("-1")
        t -= 1


main()
