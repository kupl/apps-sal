for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    maxx = 0
    ans = 0
    for i in range(1, max(arr) + 1):
        temp = 0
        ind = 0
        for j in range(N):
            if i == arr[j] and temp == 0:
                temp += 1
                ind = j
            elif i == arr[j] and j - 1 != ind:
                temp += 1
                ind = j
        if temp > maxx:
            maxx = temp
            ans = i
    print(ans)
