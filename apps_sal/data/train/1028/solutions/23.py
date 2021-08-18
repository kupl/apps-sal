for a0 in range(int(input())):
    n = int(input())
    l = list(str(n))
    q = len(l)
    s = 0
    for i in l:
        s += int(i)**q
    if s == n:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
