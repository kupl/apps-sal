t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    li = bo = 0
    c = 1
    while True:
        li = li + c
        bo = bo + c + 1
        c += 2
        if li > a:
            print("Bob")
            break
        elif bo > b:
            print("Limak")
            break
