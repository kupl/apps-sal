t = int(input())
for i in range(t):
    a = input()
    b = list(a)
    c = 0
    for i in b:
        if a.count(i) > 1:
            c = c + 1
    if c >= 1:
        print("yes")
    else:
        print("no")
