lists = []
results = []
for a in range(eval(input())):
    eval(input())
    lists.append([int(x) for x in input().split()])
for element in lists:
    results = []
    for n in element:
        ns = [x[0] for x in results]
        if n in ns :
            results[ns.index(n)][1] += 1
        else:
            results.append([n, 1])
    results.sort(key = lambda x:x[0])
    results.sort(key = lambda x:x[1], reverse = True)
    print(" ".join([str(x) for x in results[0]]))
