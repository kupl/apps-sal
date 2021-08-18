num = [x for x in range(1, 101)]
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if n % 2 != 0:
        c = n // 2
        if l[0] == 1 and l[-1] == 1:
            d = 0
            for i in range(1, c + 1):
                if l[i] - l[i - 1] == 1:
                    d = d + 1
            for i in range(c, n - 1):
                if l[i] - l[i + 1] == 1:
                    d = d + 1
            if d == n - 1:
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")
