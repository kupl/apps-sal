def arrange(n, l):
    list1 = [0] * n
    i = 0
    list2 = [-1] * n
    for j in range(n):
        if i != j:
            if i < n and list1[i] == 1:
                for k in range(i, n):
                    i += 1
                    if i < n and list1[i] != 1:
                        break
            if i == n:
                break
            else:
                if l[j] != l[i]:
                    list2[i] = l[j]
                    list2[j] = l[i]
                    list1[i] = 1
                    list1[j] = 1
                    i += 1
    if i != n:
        for j in range(0, i):
            if i < n and list1[i] == 1:
                for k in range(i, n):
                    i += 1
                    if i < n and list1[i] != 1:
                        break
            if i == n:
                break
            else:
                if l[j] != l[i] and list2[j] != l[i]:
                    list2[i] = list2[j]
                    list2[j] = l[i]
                    list1[i] = 1
                    i += 1
    if i != n:
        print('No')
    else:
        print('Yes')
        for j in list2:
            print(j, end=' ')
        print()


t = int(input())
for i in range(t):
    N = int(input())
    l = []
    s = input().split(' ')
    for j in range(N):
        l.append(int(s[j]))
    arrange(N, l)
