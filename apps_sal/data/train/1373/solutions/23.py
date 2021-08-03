for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i, j, ans = 0, 0, 0
    s = set()
    while(i < n and j < n):
        s.add(arr[j])
        if(len(s) < k):
            ans = max(ans, j - i + 1)
            j += 1
        else:
            b = arr[i]
            i += 1
            if(b not in arr[i:j + 1] and b in s):
                s.remove(b)
    print(ans)
