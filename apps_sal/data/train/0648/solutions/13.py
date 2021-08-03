n, q = list(map(int, input().split()))
arr = list(map(int, input().split()))
for _ in range(q):
    ar = list(map(int, input().split()))
    a = ar[0]
    if(a == 1):
        b, c = ar[1], ar[2]
        curr = b - 1
        f = 1
        for i in range(c):
            for j in range(curr, n):
                if(arr[j] > arr[curr] and (j - curr <= 100)):
                    curr = j
                    break

        print(curr + 1)

    else:
        b, c, d = ar[1], ar[2], ar[3]
        for k in range(b - 1, c):
            arr[k] += d
