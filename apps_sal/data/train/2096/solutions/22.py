n = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a)
d = {}
for i in range(len(a)):
    d[sorted_a[i]] = i
for i in range(len(a)):
    a[i] = d[a[i]]

res = []
done = [False] * n
for i in a:
    if done[i]:
        continue
    done[i] = True
    curr_subseq = set([i])
    next_item = a[i]
    while next_item not in curr_subseq:
        curr_subseq.add(next_item)
        done[next_item] = True
        next_item = a[next_item]
    res.append(curr_subseq)

print(len(res))
for i in res:
    curr = [str(j + 1) for j in list(i)]
    print(len(curr), end=' ')
    print(' '.join(curr))
