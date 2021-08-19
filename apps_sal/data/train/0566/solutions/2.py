t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = 0
    for i in a:
        if i in b:
            c = 1
            break
        else:
            continue
    if c == 1:
        print('Yes')
    else:
        print('No')
