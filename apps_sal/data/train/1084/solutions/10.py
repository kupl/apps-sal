t = 1
for _ in range(t):
    a = input()
    count = 1
    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            count += 1
    if a[len(a) - 1] == '0':
        count -= 1
    print(count)
