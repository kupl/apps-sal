NEIGHBOURHOOD = {"von_neumann": 1, "moore": 2}


def closer_cells(n, x, y):
    return ((x + u, y + v)
            for u in range(-1, 2) for v in range(-1, 2)
            if 0 < abs(u) + abs(v) <= n)


def get_neighbourhood(n_type, arr, coordinates):
    def is_inside(x, y):
        return 0 <= x < len(arr) and 0 <= y < len(arr[0])

    return [] if not is_inside(*coordinates) else [arr[x][y]
                                                   for x, y in closer_cells(NEIGHBOURHOOD[n_type], *coordinates)
                                                   if is_inside(x, y)]
