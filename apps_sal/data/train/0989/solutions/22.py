# cook your dish here
for _ in range(int(input())):
    x, y, k = list(map(int, input().split()))
    total = x + y

    rounds = total // k

    if rounds & 1 == 0:
        print("Chef")
    else:
        print("Paja")
