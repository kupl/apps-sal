t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    prev = ''
    count = 0
    for i in s:
        if i == prev:
            count += 1
        else:
            prev = i
    print(count)
