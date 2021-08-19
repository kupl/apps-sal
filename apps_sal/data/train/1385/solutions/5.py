def __starting_point():
    t = int(input())
    for _ in range(t):
        (n, p) = input().split()
        (n, p) = (int(n), int(p))
        s = input()
        (a, b) = (0, 0)
        arr = [0] * n
        for i in range(n):
            arr[i] = s[i]
        for c in s:
            if c == 'a':
                a += 1
            else:
                b += 1
        swap = 0
        for i in range(a):
            if s[i] == 'b':
                swap += 1
        tmpp = p
        if p <= swap:
            for i in range(n):
                if p == 0:
                    break
                if arr[i] == 'b':
                    arr[i] = 'a'
                    p -= 1
            p = tmpp
            for i in range(n - 1, -1, -1):
                if p == 0:
                    break
                if arr[i] == 'a':
                    arr[i] = 'b'
                    p -= 1
            for c in arr:
                print(c, end='')
            print()
        else:
            for i in range(n):
                if i < a:
                    arr[i] = 'a'
                else:
                    arr[i] = 'b'
            p -= swap
            for i in range(n):
                if arr[i] == 'b':
                    if s[i] == 'b' and p >= 2:
                        p -= 2
                        arr[i] = 'a'
                    if s[i] == 'a' and p >= 1:
                        p -= 1
                        arr[i] = 'a'
            for c in arr:
                print(c, end='')
            print()


__starting_point()
