for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ing = [l[0]]
    count = []
    c = 1
    d = l[0]
    ans = "YES"
    for i in l[1:]:
        if d == i:
            c += 1
        else:
            if c not in count and (i not in ing):
                count.append(c)
                c = 1
                d = i
                ing.append(d)
            else:
                ans = "NO"
                break
        # print(ing,count)
    if c in count:
        ans = "NO"
    print(ans)
