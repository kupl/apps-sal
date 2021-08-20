t = int(input())
while t:
    k = int(input())
    s = input()
    n = 4
    l = [s[i:i + n] for i in range(0, k, n)]
    li = []
    for i in l:
        li.append(chr(int(i, 2) + 97))
    print(''.join((i for i in li)))
    t -= 1
