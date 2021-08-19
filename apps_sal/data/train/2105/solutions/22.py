def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
ans = []
for i in range(2, n + 2):
    if is_prime(i):
        ans.append(1)
    else:
        ans.append(2)
if n == 1:
    print(1)
    print(1)
elif n == 2:
    print(1)
    print(1, 1)
else:
    print(2)
    print(' '.join((str(num) for num in ans)))
