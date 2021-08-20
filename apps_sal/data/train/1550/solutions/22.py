def binary(x):
    result = []
    while x != 0:
        temp = x % 2
        x = x // 2
        result.append(temp)
    return result


def binCount(x):
    count = 0
    while x != 0:
        x = x // 2
        count += 1
    return count


def xnor(a, b):
    final = []
    count = max(binCount(a), binCount(b))
    abin = binary(a)
    bbin = binary(b)
    if count != len(abin):
        while len(abin) != count:
            abin.append(0)
    if count != len(bbin):
        while len(bbin) != count:
            bbin.append(0)
    i = 0
    while i < count:
        if bbin[i] == 0 and abin[i] == 0 or (bbin[i] == 1 and abin[i] == 1):
            final.append(1)
        else:
            final.append(0)
        i += 1
    ans = 0
    i = 0
    for dig in final:
        ans += dig * 2 ** i
        i += 1
    return ans


tulu = int(input())
for _ in range(tulu):
    (a, b, n) = [int(x) for x in input().split()]
    x = a ^ b
    y = xnor(a, b)
    value1 = x
    value2 = y
    if n % 3 == 1:
        value1 = a
        value2 = a
    if n % 3 == 2:
        value2 = b
        value1 = b
    print(max(value1, value2))
