for _ in range(int(input())):
    num = int(input())
    if num % 10 == 0:
        ans = 0
    elif num % 5 == 0:
        ans = 1
    else:
        ans = -1
    print(ans)
