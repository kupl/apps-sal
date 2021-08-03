for _ in range(int(input())):
    n = input()
    ans = sum(list(map(int, n)))
    if(len(n) > 1 and ans < 9):
        print(9 - ans)
    else:
        print(min(ans % 9, 9 - ans % 9))
