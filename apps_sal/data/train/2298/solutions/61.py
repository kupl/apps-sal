(N, T) = map(int, input().split())
a = list(map(int, input().split()))
x = 10**9
d = 0
counter = 0
for i in a:
    if i < x:
        x = i
    elif i - x > d:
        d = i - x
        counter = 1
    elif i - x == d:
        counter += 1
print(counter)
