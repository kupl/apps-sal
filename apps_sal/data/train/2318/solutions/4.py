def f():
    return map(int, input().split())


(n, k) = f()
j = 0
for (i, q) in enumerate(f(), 1):
    if j * (i - n) * q < k:
        print(i)
    else:
        k -= q * j
        j += 1
