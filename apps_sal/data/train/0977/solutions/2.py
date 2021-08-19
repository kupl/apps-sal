for t in range(int(input())):
    n = int(input())
    a = list(input())
    l = 'abcdefghijklmnopqrstuvwxyz'
    q = 'zyxwvutsrqponmlkjihgfedcba'
    if n % 2 == 0:
        c = 0
        while c < n:
            temp = a[c]
            a[c] = a[c + 1]
            a[c + 1] = temp
            c += 2
        for i in range(0, n):
            for j in range(0, len(l)):
                if a[i] == l[j]:
                    print(q[j], end='')
                    break
    else:
        c = 0
        while c < n - 1:
            temp = a[c]
            a[c] = a[c + 1]
            a[c + 1] = temp
            c += 2
        for i in range(0, n):
            for j in range(0, len(l)):
                if a[i] == l[j]:
                    print(q[j], end='')
                    break
    print('\r')
