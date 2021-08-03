def get_mini(n, ls):
    ls = sorted(ls)[::-1]
    first_burner = 0
    second_burner = 0
    for i in range(n):
        if first_burner <= second_burner:
            first_burner += ls[i]
        else:
            second_burner += ls[i]
    return max(first_burner, second_burner)


t = int(input())
for _ in range(t):
    n = int(input())
    dish = list(map(int, input().split()))
    ans = get_mini(n, dish)
    print(ans)
