def fit_bag(height: int, width: int, items: [[[int]]]) -> [[int]]:

    def get_box_size(a): return len(a) * len(a[0])
    items.sort(key=get_box_size, reverse=True)

    def arrange(partial_bag: [[int]], ind_item: int) -> [[int]]:

        if ind_item == len(items):
            return partial_bag

        cur_item = items[ind_item]
        for r in range(height - len(cur_item) + 1):
            for c in range(width - len(cur_item[0]) + 1):
                if fits(partial_bag, cur_item, r, c):
                    new_bag = arrange(combine(partial_bag, cur_item, r, c), ind_item + 1)
                    if new_bag:
                        return new_bag

    def fits(b1, b2, r, c) -> bool:
        for ir in range(r, r + len(b2)):
            for ic in range(c, c + len(b2[0])):
                if b1[ir][ic] and b2[ir - r][ic - c]:
                    return False
        return True

    def combine(b1, b2, r, c) -> [[int]]:
        new_bag = []
        for ir in range(height):
            new_bag.append(b1[ir][:])
        for ir in range(r, r + len(b2)):
            for ic in range(c, c + len(b2[0])):
                new_bag[ir][ic] += b2[ir - r][ic - c]
        return new_bag

    return arrange([[0] * width for _ in range(height)], 0)
