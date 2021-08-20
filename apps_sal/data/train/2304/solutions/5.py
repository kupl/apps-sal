d = 10 ** 9 + 7
n = int(input())
p = [0] * 5001
p[len(input())] = 1
while n:
    p = [((2 * p[j - 1] if j else p[j]) + p[j + 1]) % d for j in range(n)]
    n = n - 1
print(p[0])
