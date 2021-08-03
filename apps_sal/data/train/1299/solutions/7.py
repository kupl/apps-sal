try:
    for _ in range(int(input())):
        n1 = int(input())
        list2 = list(map(int, input().split()))
        set1 = set(list2)
        list3 = []
        list4 = [list2[0]]
        list5 = []
        for i in set1:
            list3.append(i)
        list3.sort()
        m = 0
        n = list2[0]
        for i in range(1, len(list2)):
            if(list2[i] != n or i - m > 1):
                list4.append(list2[i])
                m = i
                n = list2[i]
        for i in range(len(list3)):
            list5.append(list4.count(list3[i]))
        val = list5.index(max(list5))
        print(list3[val])
except:
    pass
