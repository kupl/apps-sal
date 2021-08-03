# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if l[0] == 0:
        print(0)
    else:
        s = l[0]
        c = 0
        for i in range(1, len(l)):
            s -= 1
            s += l[i]
            c += 1
            if s == 0:
                break
        print(s + c)
