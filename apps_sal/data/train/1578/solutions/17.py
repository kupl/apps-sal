t = int(input().strip())
for _ in range(t):
    p = input().strip()
    count = 0
    for i in p:
        if not 'a' <= i <= 'z':
            count += int(i)
    print(count)
