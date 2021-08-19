# cook your dish here
t = int(input())
while t > 0:
    n, a, b, k = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if i % a == 0 and i % b != 0:
            c = c + 1
        if i % b == 0 and i % a != 0:
            c = c + 1
    if c >= k:
        print("Win")
    else:
        print("Lose")
    t = t - 1
