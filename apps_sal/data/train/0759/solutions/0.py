# cook your dish here
store = [0] * (10**5 + 1)


def sieve():
    for i in range(2, 10**5 + 1):
        if(store[i] == 0):
            store[i] = 1
            for j in range(i, 10**5 + 1, i):
                store[j] = i


sieve()
# print(store)
for _ in range(int(input())):

    n = int(input())
    li = [int(x) for x in input().split()]

    dp = [0] * (10**5 + 1)
    for i in li:
        dp[store[i]] += 1
    max_re = 0
    res = 0
    for i in li:
        if(dp[store[i]] == max_re):
            if(store[i] > res):
                res = store[i]
        elif(dp[store[i]] > max_re):
            max_re = dp[store[i]]
            res = store[i]

    print(res)
