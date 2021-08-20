for _ in range(int(input())):
    (a, b) = [int(i) for i in input().split()]
    tot = 0
    ans = []
    for i in range(1, 11):
        ans.append(int(str(b * i)[-1]))
    tot = sum(ans)
    x = a // b
    y = x % 10
    x = x // 10
    ans = tot * x + sum(ans[:y])
    print(ans)
