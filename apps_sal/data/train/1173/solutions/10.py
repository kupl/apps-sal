def sumPairs(arr, n):
    sum = 0
    for i in range(n - 1, -1, -1):
        sum += i * arr[i] - (n - 1 - i) * arr[i]
    return sum - ((n * (n - 1)) // 2)


def R(): return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n = int(input())
    xs = list(map(int, input().split()))
    xor = 0
    dict = {0: [0]}
    count = 0
    i = 0
    for x in xs:
        xor = xor ^ x
        if xor not in dict:
            dict[xor] = [i + 1]
        else:
            dict[xor].append(i + 1)
        i += 1
    ans = 0
    for i in list(dict.values()):
        if len(i) == 1:
            continue
        else:
            ans += (sumPairs(i, len(i)))

    print(ans)
