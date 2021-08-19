n = int(eval(input()))
for i in range(0, n):
    (a, b) = list(map(int, input().split()))
    r = a % b
    print(r)
