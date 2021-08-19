# cook your dish here
t = int(input())
for i in range(t):
    a, b = list(input().split())
    l = []
    for i in range(int(a)):
        l.append(input())
    # print(l)
    r = 0
    r1 = 0
    for i in range(len(l)):
        if l[i][0] == "0":
            r += l[i].count("0")
        else:
            r1 += l[i].count("1")
    if b == "Dee":
        if r > r1:
            print("Dee")
        else:
            print("Dum")
    else:
        if r1 > r:
            print("Dum")
        else:
            print("Dee")
