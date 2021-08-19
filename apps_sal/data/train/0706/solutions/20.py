for _ in range(int(input())):
    (w, k) = list(map(int, input().split()))
    l = list(map(int, input().split()))
    if max(l) <= k:
        i = 0
        r = 0
        while i < w:
            a = 0
            for j in range(w - i):
                a += l[i + j]
                if a > k:
                    j -= 1
                    break
            r += 1
            i += j + 1
        print(r)
    else:
        print(-1)
