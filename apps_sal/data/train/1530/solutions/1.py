t = int(input())
for i in range(0, t):
    n = int(input().strip())
    val = 1
    for xyz in range(1, n + 1):
        list1 = list()
        for abc in range(1, xyz + 1):
            list1.append(val)
            val += 1
        print(*list1[::-1], sep='')
        print()
        list1.clear()
