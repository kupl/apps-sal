t = int(input())
while t > 0:
    l, b = map(int, input().split(" "))
    li = bo = 0
    c = 1
    while True:
        li = li + c
        bo = bo + c + 1
        c += 2
        if li > l:
            print("Bob")
            break
        elif bo > b:
            print("Limak")
            break
    t -= 1
