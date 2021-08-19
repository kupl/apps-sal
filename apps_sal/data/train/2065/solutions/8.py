(n, k) = list(map(int, input().split()))
m = [0] * k
f = 0
for y in range(k):
    m = list(map(int, input().split()))[1:]
    i = 0
    while i < len(m):
        if m[i] == 1:
            if i > 0:
                f += 1
            j = i + 1
            while j < len(m):
                if m[j] - m[j - 1] != 1:
                    f += 1
                    break
                j += 1
            i = j
        elif i > 0:
            f += 1
        i += 1
print(2 * f + k - 1)
