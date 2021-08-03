a = int(input())
while a:
    a = a - 1
    b = int(input())
    x = list(map(int, input().split()))
    p = []
    for i in x:
        if i not in p:
            p.append(i)
    print(len(p))
