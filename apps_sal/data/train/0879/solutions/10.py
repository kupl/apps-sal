for _ in range(int(input())):
    (x, y) = map(int, input().split())
    strength = 0
    for i in range(y, x + 1, y):
        strength += i % 10
    print(strength)
