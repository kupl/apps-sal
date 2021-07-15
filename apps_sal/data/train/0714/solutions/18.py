try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        s = sum(arr)
        count = 0
        if s%n==0:
            each = s//n
        else:
            each = (s//n)+1
        for i in range(n):
            if arr[i]<each:
                count += (each - arr[i])
        print(count)
except EOFError:
    pass
