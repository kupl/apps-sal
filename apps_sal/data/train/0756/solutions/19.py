t = int(input())
for i in range(t):
    (x, y) = map(int, input().split())
    sum1 = x + y + 1
    sum2 = sum1
    while True:
        if sum1 % 2 != 0:
            for j in range(3, sum1, 2):
                if sum1 % j == 0:
                    sum1 += 2
                    break
            else:
                print(sum1 - sum2 + 1)
                break
        else:
            sum1 += 1
