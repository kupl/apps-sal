for _ in range(int(input())):
    lens = int(input())
    arrs = [int(x) for x in input().split()]
    ans = min([abs(y - x) for x, y in zip(arrs, arrs[1:])])
    print(ans)
