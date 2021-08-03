n = int(input())
a = [int(i) for i in input().split()]
a = [i[0] for i in sorted(enumerate(a), key=lambda x:x[1])]
checker = [0 for i in range(n)]
ans_set = []
for i in range(n):
    if checker[i] == 0:
        tmp = set([i])
        next_step = i
        next_step = a[next_step]
        while next_step != i:
            checker[next_step] = 1
            tmp.add(next_step)
            next_step = a[next_step]
        ans_set.append(tmp)
print(len(ans_set))
for tmp in ans_set:
    print(len(tmp), end=" ")
    for j in tmp:
        print(j + 1, end=" ")
    print()
