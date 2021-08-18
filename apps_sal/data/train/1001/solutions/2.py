n = int(input())
list2 = [751, 751, 751, 751, 751]
for i in range(n):
    x = int(input())
    list1 = list(map(int, (input().split())))
    list1 = list2 + list1
    p = 0
    for i in range(5, len(list1)):
        a = list1[i - 5]
        b = list1[i - 4]
        c = list1[i - 3]
        d = list1[i - 2]
        e = list1[i - 1]
        f = list1[i]
        r = min(a, b, c, d, e)
        if f < r:
            p += 1
    print(p)
