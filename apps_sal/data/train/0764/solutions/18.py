t = int(input())
while t > 0:
    s = input()
    l1 = list(s.split(" "))
    s = input()
    l2 = list(s.split(" "))
    l = len(l1)
    l = l // 2
    c = fl = 0
    for i in range(0, len(l1)):
        if l1[i] in l2:
            c += 1
        if c == 2:
            fl = 1
            break
    if fl == 1:
        print("similar")
    else:
        print("dissimilar")
    t -= 1
