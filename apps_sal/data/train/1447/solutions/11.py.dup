for _ in range(int(input())):
    n = int(input())
    val = [int(x) for x in input().split()]
    ing = [val[0]]
    count = []
    c = 1
    prev = val[0]
    ans = "YES"
    for i in val[1:]:
        if prev == i:
            c += 1
        else:
            if c not in count and (i not in ing):
                count.append(c)
                c = 1
                prev = i
                ing.append(prev)
            else:
                ans = "NO"
                break

    if c in count:
        ans = "NO"
    print(ans)
