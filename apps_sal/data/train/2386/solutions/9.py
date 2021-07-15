t = int(input())
for tc in range(t):
    n = int(input())
    lst = input().split()
    ans = []
    ansl = 0
    for i in lst :
        if i not in ans :
            ans.append(i)
            if len(ans) >= n :
                break
    for i in ans :
        print(i, end = " ")
    print()
