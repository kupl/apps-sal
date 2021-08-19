tests = int(input())
for test in range(tests):
    (n, k) = list(map(int, input().strip().split(' ')))
    if k > n:
        print(0)
    else:
        r = 1
        a = k
        b = n - k
        todo = []
        for i in range(1, min(a, b) + 1):
            todo += [i]
        j = 0
        i = max(a, b) + 1
        while i <= n:
            r *= i
            while j < len(todo) and r % todo[j] == 0:
                r /= todo[j]
                j = j + 1
            i = i + 1
        for i in range(j, len(todo)):
            r /= todo[i]
        print(r)
