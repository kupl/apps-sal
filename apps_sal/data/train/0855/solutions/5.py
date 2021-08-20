t = int(input())
while t > 0:
    st = input()
    for i in range(0, len(st)):
        print(st[len(st) - 1 - i], end='')
    t -= 1
