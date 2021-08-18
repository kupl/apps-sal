t = int(input())
i = 0
while i < t:
    c = 0
    d = list(input().strip())
    s = set(d)
    n = int(input())
    k = input()
    lst = list(k.split())
    for j in s:
        if j in lst:
            continue
        else:
            c += 1
            break
    if c == 0:
        print("1")
    else:
        print("0")
    i += 1
