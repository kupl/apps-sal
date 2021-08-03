a = int(input())
while a:
    a = a - 1
    b, c = list(map(int, input().split()))
    l = 0
    t = 0
    k = 1
    h = 2
    while 1:
        if l + k > b:
            print("Bob")
            break
        elif t + h > c:
            print("Limak")
            break
        else:
            l = l + k
            t = t + h
            k = k + 2
            h = h + 2
