n = 100000
li = [0] * n
store = []
for i in range(1, n):
    for j in range(i - 1, n, i):
        li[j] ^= 1
    store.append(li)


def doors(n): return store[n + 1][:n].count(1)
