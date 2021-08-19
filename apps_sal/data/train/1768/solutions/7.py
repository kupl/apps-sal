def fit_bag(height, width, items):
    nitems = len(items)
    blocks = sorted([(item, sum((j != 0 for i in item for j in i))) for item in items], key=lambda x: -x[1])

    def place(block_id, bag, remain):
        if block_id >= len(blocks):
            return
        (item, item_size) = blocks[block_id]
        (m, n) = (len(item), len(item[0]))
        offsets = [(i, j) for i in range(height - m + 1) for j in range(width - n + 1)]
        values = [(i, j, c) for (i, row) in enumerate(item) for (j, c) in enumerate(row) if c != 0]
        for (dx, dy) in offsets:
            newbag = list(map(list, bag))
            for (i, j, c) in values:
                if newbag[i + dx][j + dy] == 0:
                    newbag[i + dx][j + dy] = c
                else:
                    break
            else:
                yield (newbag, remain - item_size, block_id + 1)
    s = [([[0] * width for i in range(height)], height * width, 0)]
    while s:
        (current, remain, block_id) = s.pop()
        if block_id == nitems:
            return current
        for v in place(block_id, current, remain):
            s.append(v)
