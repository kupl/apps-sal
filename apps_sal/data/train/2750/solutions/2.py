def make_sequences(n):
    a = [1]
    for i in range(1, n + 1):
        a.append(a[i - 1] if i % 2 else a[i // 2] + a[i - 1])
    return a.pop()
