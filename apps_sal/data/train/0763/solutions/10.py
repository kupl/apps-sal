t = int(input())
for i in range(t):
    n = input()
    l = input()
    p = input()
    c = 1
    o = 0
    z = 0
    for j in range(len(l)):
        if l[j] != p[j]:
            if l[j] == "1":
                o += 1
            else:
                z += 1
            if o < z:
                c = 0
                break
    if c == 1 and o == z:
        print("Yes")
    else:
        print("No")
