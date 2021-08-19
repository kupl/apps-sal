n = int(input())
for i in range(n):
    a = input()
    b = input()
    c = 0
    for i in a:
        if i in b:
            c = 1
            print('Yes')
            break
    if c == 0:
        print('No')
