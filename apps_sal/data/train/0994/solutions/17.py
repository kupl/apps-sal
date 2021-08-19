try:
    import math
    for _ in range(int(input())):
        (n, x) = list(map(int, input().split()))
        list1 = list(map(int, input().split()))
        ll = set()
        for i in range(1, int(math.sqrt(x)) + 1):
            if x % i == 0:
                if i <= n:
                    ll.add(i)
                if x // i <= n:
                    ll.add(x // i)
        for i in range(1, n):
            list1[i] = list1[i] + list1[i - 1]
        c = 0
        for i in ll:
            a = i
            y = x // a
            list2 = []
            j = -1
            for i in range(a - 1, n):
                if j == -1:
                    list2.append(list1[i])
                    j += 1
                else:
                    list2.append(list1[i] - list1[j])
                    j += 1
            for k in list2:
                c += list2.count(y - k)
        print(c)
except:
    pass
