T = int(input())

for _ in range(T):
    N = int(input())
    cars = list(map(int, input().split()))
    ans = 0
    for i in range(len(cars)):
        if i == 0:
            ans += 1
        else:
            if cars[i - 1] < cars[i]:
                cars[i] = cars[i - 1]
            else:
                ans += 1
    print(ans)
