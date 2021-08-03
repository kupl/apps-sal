# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    p = input()
    c = 1
    o = 0
    z = 0
    for j in range(n):
        if s[j] != p[j]:
            if s[j] == "1":
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
