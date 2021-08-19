for _ in range(int(input())):
    (n, p) = map(int, input().split())
    s = list(input())
    a = s.count('a')
    b = s.count('b')
    swap = 0
    arr = [i for i in s]
    for i in range(a):
        if s[i] == 'b':
            swap += 1
    if p <= swap:
        i = 0
        tmp = p
        while p > 0 and i < n:
            if arr[i] == 'b':
                arr[i] = 'a'
                p -= 1
            i += 1
        p = tmp
        i = n - 1
        while p > 0 and i > 0:
            if arr[i] == 'a':
                arr[i] = 'b'
                p -= 1
            i -= 1
        print(''.join(arr))
    else:
        for j in range(n):
            if j < a:
                arr[j] = 'a'
            else:
                arr[j] = 'b'
        p -= swap
        for k in range(n):
            if arr[k] == 'b':
                if s[k] == 'b' and p >= 2:
                    p -= 2
                    arr[k] = 'a'
                if s[k] == 'a' and p >= 1:
                    p -= 1
                    arr[k] = 'a'
        print(''.join(arr))
