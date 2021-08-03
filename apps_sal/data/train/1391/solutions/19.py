from sys import stdin, stdout
tc = int(stdin.readline())
for i in range(tc):
    n, k = list(map(int, stdin.readline().split()))
    dict1 = {}
    comp_to_iterate = []
    for j in range(n):
        s, f, comp = list(map(int, stdin.readline().split()))
        if comp in dict1.keys():
            dict1[comp].append((s, f))
            if comp not in comp_to_iterate:
                comp_to_iterate.append(comp)
        else:
            dict1[comp] = [(s, f)]
    total = len(dict1.keys()) - len(comp_to_iterate)
    for key in comp_to_iterate:
        value = dict1[key]
        value.sort(key=lambda x: x[1])
        el = value[0]
        l = 1
        total += 1
        while l < len(value):
            if value[l][0] >= el[1]:
                total += 1
                el = value[l]
            l += 1
    print(total)
