def fit_bag(height: int, width: int, items: List[List[List[int]]]) -> List[List[int]]:
    result = [[0] * width for _ in range(height)]

    def check(i, j, item):
        return not any(x and result[i + k][j + l] for k, row in enumerate(item) for l, x in enumerate(row))

    def place(i, j, item):
        for k, row in enumerate(item):
            for l, x in enumerate(row):
                if x != 0:
                    result[i + k][j + l] = x

    def remove(i, j, item, id):
        for k, row in enumerate(item):
            for l, x in enumerate(row):
                if x == id:
                    result[i + k][j + l] = 0

    def rec(item_id=0):
        if item_id == len(items):
            return True
        item = items[item_id]
        h, w = len(item), len(item[0])
        id = next(x for row in item for x in row if x)
        for i in range(height - h + 1):
            for j in range(width - w + 1):
                if check(i, j, item):
                    place(i, j, item)
                    if rec(item_id + 1):
                        return True
                    remove(i, j, item, id)
        return False

    rec()
    return result
