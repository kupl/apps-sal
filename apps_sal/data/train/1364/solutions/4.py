import collections
t = int(input())
for _ in range(t):
    (n, c) = list(map(int, input().split()))
    hashmap = collections.defaultdict(list)
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        hashmap[x - y, x % c].append(x)
    steps = 0
    total = 0
    for each in hashmap:
        hashmap[each].sort()
        med = hashmap[each][len(hashmap[each]) // 2]
        for val in hashmap[each]:
            total += abs(med - val)
    print(len(hashmap), total // c)
