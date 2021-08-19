a = int(input())
for i in range(0, a):
    s = int(input())
    j = s
    su = 0
    while j != 0:
        su = su + j ** 3
        j -= 1
    j = 1
    while j != s:
        su = su + j ** 3
        j += 1
    print(su)
