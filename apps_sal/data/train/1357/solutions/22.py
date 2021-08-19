n = int(input())
while n > 0:
    t = int(input())
    total = 0
    arr = list(map(int, input().split()))
    for i in arr:
        if i == 5:
            total += 5
        else:
            total -= i - 5
            if total < 0:
                print('NO')
                break
    else:
        print('YES')
    n -= 1
