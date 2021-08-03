for i in range(int(input())):
    x = int(input())
    s = list(input())
    ans = []
    for j in range(1, 9):
        ans.append(s.count(str(j)))

    print(min(ans))
