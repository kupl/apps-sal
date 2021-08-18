for _ in range(int(input())):
    n = int(input())
    x = int(input())
    a = list(map(int, input().split()))
    s = sorted(a)
    flag = False
    if x > n:
        for i in range(n):
            if s[i] == 1:
                break
            else:
                flag = True
    else:
        sub = 0
        b = n % x
        for i in range(n):
            if len(s) > b:
                for j in range(x):
                    a = s[0] - sub
                    if a == 1:
                        flag = False
                        break
                    else:
                        del s[0]
                        flag = True
                sub += 1
            if flag:
                pass
            else:
                break
    if flag:
        print("Possible")
    else:
        print("Impossible")
