n, k = list(map(int, input().split(' ')))
for i in range(k):
    x = input().split(' ')
    if x[1] == '1':
        y = [int(j) for j in x[1:]] + [0]
        z = 0
        while y[z + 1] == z + 2:
            z += 1
print(2 * n - k - 1 - 2 * z)
