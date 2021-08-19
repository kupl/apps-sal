n = int(input())


def is_prime(x):
    if x == 2:
        return True
    if x == 1 or x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


ans = []
for i in range(2, n + 1):
    if is_prime(i):
        j = i
        while j <= n:
            ans.append(j)
            j *= i
print(len(ans))
print(' '.join(map(str, ans)))
