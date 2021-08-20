n = int(input())
total = 0
rem = 10 ** 20
for _ in range(n):
    (a, b) = map(int, input().split())
    if a > b:
        rem = min(rem, b)
    total += b
if rem == 10 ** 20:
    print(0)
else:
    print(total - rem)
