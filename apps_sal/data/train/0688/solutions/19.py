t = int(input())
l = []
for i in range(t):
    count = 0
    a = input()
    if a[0] != a[7]:
        count += 1
    for i in range(0, 6):
        if a[i] != a[i + 1]:
            count += 1
    l.append(count)
for i in l:
    if i <= 2:
        print('uniform')
    else:
        print('non-uniform')
