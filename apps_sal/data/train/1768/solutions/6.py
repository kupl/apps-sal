def fit_bag(height: int, width: int, items: List[List[List[int]]]) -> List[List[int]]:
    bag = [[0] * width for _ in range(height)]
    return solve(bag, width, height, items)


def solve(bag, width, height, items):
    if not items:
        return bag
    item = items[0]
    (item_width, item_height) = (len(item[0]), len(item))
    for px in range(width - item_width + 1):
        for py in range(height - item_height + 1):
            new_bag = place(bag, item, item_width, item_height, px, py)
            if not new_bag:
                continue
            solution = solve(new_bag, width, height, items[1:])
            if solution:
                return solution


def place(bag, item, item_width, item_height, px, py):
    for y in range(item_height):
        for x in range(item_width):
            if item[y][x] and bag[py + y][px + x]:
                return None
    new_bag = [row.copy() for row in bag]
    for y in range(item_height):
        for x in range(item_width):
            if item[y][x]:
                new_bag[py + y][px + x] = item[y][x]
    return new_bag
