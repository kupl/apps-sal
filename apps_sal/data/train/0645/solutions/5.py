testcase = int(input())
for ij in range(testcase):
    n = int(input())
    k = int(input())
    list1 = []
    list2 = []
    list3 = [0]
    if n % 2 != 0:
        f = n // 2
        for i in range(f):
            list1.append(2 * (i + 1))
        for i in range(len(list1)):
            list2.append(list1[i])
        for i in range(len(list1)):
            list2.append(list1[f - 1 - i])

    if n % 2 == 0:
        s = (n - 1) // 2

        for i in range(s):
            list1.append(2 * (i + 1))
        for i in range(s):
            list2.append(list1[i])
        list2.append(list1[s - 1] + 1)
        for i in range(s):
            list2.append((list1[s - 1 - i]))
    list2.append(0)

    p = k % n
    print(list2[p - 1])
