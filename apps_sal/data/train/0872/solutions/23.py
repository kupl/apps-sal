t = int(input())
while t > 0:
    (n, a, b, k) = map(int, input().split())
    prob = 0
    if a == 1 and b == 1:
        print('Lose')
    else:
        for i in range(1, n + 1):
            if i % a == 0 and i % b == 0:
                continue
            elif i % a == 0 and i % b != 0:
                prob += 1
            elif i % b == 0 and i % a != 0:
                prob += 1
        if prob >= k:
            print('Win')
        else:
            print('Lose')
    t -= 1
