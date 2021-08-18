def count(arr):
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 1:
            even += 1
        else:
            odd += 1
    return (even - 1) * even // 2 + (odd - 1) * odd // 2


def solve(a):
    sums = []
    x = 0
    for i in a:
        x = x ^ i
        sums.append(x)
    d = {}
    d[0] = [-1]
    for i in range(len(sums)):
        if sums[i] in d:
            d[sums[i]].append(i)
        else:
            d[sums[i]] = [i]
    res = 0
    for sums in d:
        res += count(d[sums])
    return res


n = int(input())
x = input().split()
a = []
for i in x:
    a.append(int(i))
print(solve(a))
