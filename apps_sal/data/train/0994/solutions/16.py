try:
    import math
    from collections import defaultdict
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
            dict1 = {}
            for i in range(a - 1, n):
                if j == -1:
                    list2.append(list1[i])
                    if list1[i] in dict1:
                        dict1[list1[i]] += 1
                    else:
                        dict1[list1[i]] = 1
                    j += 1
                else:
                    list2.append(list1[i] - list1[j])
                    if list1[i] - list1[j] in dict1:
                        dict1[list1[i] - list1[j]] += 1
                    else:
                        dict1[list1[i] - list1[j]] = 1
                    j += 1
            for k in list2:
                if y - k in dict1:
                    c += dict1[y - k]
        print(c)
except:
    pass
