t = int(input())
for _ in range(t):
    n = int(input())
    it = list(map(int, input().split()))
    x = [i for i in it if i >= n]
    if n == 1:
        print(-1)
        continue
    if len(x) > 0:
        print(-1)
        continue
    if it.count(0) == n:
        print(n)
        continue
    if n - 1 in it:
        if it == [n - 1] * n:
            print(0)
        elif it.count(n - 2) == n - 1:
            print(1)
        else:
            print(-1)
    else:
        aa = list(set(it))
        if len(aa) == 2:
            aa.sort()
            if aa[1] - aa[0] == 1:
                x = len([i for i in it if i == aa[0]])
                if x == aa[1]:
                    print(n - x)
                else:
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)
