nodes = []
start_nodes = []
for i in range(int(input().strip())):
    (left, right) = input().strip().split()
    left = int(left)
    right = int(right)
    current = i + 1
    if left == 0:
        start_nodes.append([left, current, right])
    else:
        nodes.append([left, current, right])
lists = []
for node in start_nodes:
    links = [node]
    while True:
        prevlen = len(links)
        for i in range(len(nodes)):
            if links[-1][-1] == nodes[i][1]:
                links.append(nodes[i])
        nextlen = len(links)
        if prevlen == nextlen:
            break
    lists.append(links)
flattened = [node for ll in lists for node in ll]
for i in range(1, len(flattened)):
    if flattened[i][0] == 0:
        flattened[i][0] = flattened[i - 1][1]
        flattened[i - 1][2] = flattened[i][1]
sorted_union = sorted(flattened, key=lambda x: x[1])
for node in sorted_union:
    print(node[0], node[2])
