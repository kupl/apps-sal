for t in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    con = []
    count = 1
    c = []
    i = 0
    while i < n:
        while (i < n - 1) and (arr[i] == arr[i + 1]):
            i += 1
            count += 1
        if arr[i] in con or count in c:
            break
        con.append(arr[i])
        c.append(count)
        i += 1
        count = 1

    if i == n:
        print("YES")
    else:
        print("NO")
