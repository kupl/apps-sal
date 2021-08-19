from bisect import bisect


def is_pal(s):
    return s == s[::-1]


(N, temp) = (2500, set())
for x in range(1, N):
    val = x ** 2
    for y in range(x + 1, N):
        val += y ** 2
        if val not in temp and is_pal(str(val)):
            temp.add(val)
result = sorted(temp)


def values(n):
    return bisect(result, n)
