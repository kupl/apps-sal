for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 'Poor Chef'
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] == l[j]:
                if i + 1 in l and j + 1 in l:
                    ans = 'Truly Happy'
    print(ans)
