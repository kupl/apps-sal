# cook your dish here
try:
    MAX = 1000005
    prime = [True] * MAX
    fact = [list() for i in range(MAX)]

    for i in range(2, MAX):
        if prime[i]:
            for j in range(i, MAX, i):
                prime[j] = False
                fact[j].append(i)

    def solve(arr, i, k):
        if i >= len(arr):
            return sum(k)
        z = float('inf')
        for j in range(len(k)):
            k[j] *= arr[i]
            z = min(z, solve(arr, i + 1, k))
            k[j] //= arr[i]
        return z

    t = int(input())
    for i in range(t):
        k, x = map(int, input().split())
        temp = []
        for y in fact[x]:
            p = x
            z = 1
            while p % y == 0:
                p //= y
                z *= y
            temp.append(z)
        if k >= len(fact[x]):
            print(sum(temp) + k - len(temp))
        else:
            print(solve(temp, 0, [1] * k))

except EOFError as e:
    pass
