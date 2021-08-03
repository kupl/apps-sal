q = int(input())
for i in range(q):
    n = int(input())
    a = [int(x) for x in input().split()]
    dic = {}
    b = []
    counter = 0
    for item in a:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    for item in dic:
        b.append(dic[item])
    b.sort(reverse=True)
    x = b[0] + 1
    for item in b:
        x = min(x - 1, item)
        counter += max(x, 0)
    print(counter)
