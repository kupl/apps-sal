t = int(input())
for i in range(t):
    n = int(input())
    list1 = []
    for i in range(n):
        s = input()
        for i in range(len(s)):
            list1.append(s[i])
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0
    t1 = list1.count('c') // 2
    t2 = list1.count('o') // 1
    t3 = list1.count('d') // 1
    t4 = list1.count('e') // 2
    t5 = list1.count('h') // 1
    t6 = list1.count('f') // 1
    print(min(t1, t2, t3, t4, t5, t6))
