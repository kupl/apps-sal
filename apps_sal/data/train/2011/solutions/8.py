def summ(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s


(n, count, a) = (int(input()), 0, [])
for i in range(max(1, n - 81), n):
    if summ(i) + i == n:
        count += 1
        a.append(i)
print(count)
for i in a:
    print(i)
