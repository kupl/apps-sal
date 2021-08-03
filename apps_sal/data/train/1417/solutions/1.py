for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dic = {}
    for i in range(1, 9):
        dic[i] = a.count(i)
    ans = min(dic.values())
    print(ans)
