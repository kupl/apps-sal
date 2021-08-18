def christmas_tree(height):
    height, tree = height // 3, []
    for floor in range(height):
        for branch in range(floor, 3 + floor):
            tree.append(f"{' ' * (height - branch + 1)}{'*' * (branch * 2 + 1)}")
    tree.append(f"{' ' * (height)}
    return "\r\n".join(tree) if height else ""
