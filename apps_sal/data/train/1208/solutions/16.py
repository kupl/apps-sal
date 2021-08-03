try:
    m = 10**9 + 7

    def jk(n):
        count = 1
        arr = []
        ans = [1]

        for i in range(1, n + 1):
            count = (count * i) % m
            arr.append(count)

        for i in range(1, len(arr)):
            ans.append((ans[-1] * arr[i]) % m)

        return ans

    t = jk(10**6)
    for _ in range(int(input())):
        num = int(input())
        print(t[num - 1])

except:
    pass
