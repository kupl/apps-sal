s = input()

if s[0] == '0' or s[-2] == '0' or s[-1] == '1':  # 's' should be like "1xx...x0"
    print((-1))
elif s[:-1] != s[-2::-1]:
    print((-1))
else:
    half = len(s) // 2
    one_indices = [i + 1 for i in range(1, half) if s[i] == '1']  # not including 0 or larger than n//2

    parents = [0] * (len(s) + 1)
    parent_index = 1
    for index in one_indices:
        for i in range(parent_index, index):
            parents[i] = index
        parent_index = index

    root = parent_index + 1
    parents[parent_index] = root
    for index in range(root + 1, len(s) + 1):
        parents[index] = root

    for node, parent in enumerate(parents):
        if parent == 0:  # This means node is 0 or the root of the tree.
            continue
        print((node, parent))
