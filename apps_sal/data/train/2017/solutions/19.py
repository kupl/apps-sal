_ = int(input())
ns = list(map(int, input().split()))
seen = [False for _ in range(len(ns) // 2 + 1)]
count = 0
index = 0
while index != len(ns):
    e = ns[index]
    if seen[e]:
        while ns[index - 1] != e:
            ns[index], ns[index - 1] = ns[index - 1], ns[index]
            seen[ns[index]] = False
            count += 1
            index -= 1
            # print(ns)
    seen[e] = True
    index += 1
print(count)
