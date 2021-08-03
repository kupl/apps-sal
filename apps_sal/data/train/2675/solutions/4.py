def bad_apples(a):
    li, visited = [], []
    for i, j in enumerate(a):
        if i not in visited and sum(j) != 0:
            if 0 in j:
                find = next((k for k in range(i + 1, len(a))if 0 in a[k] and sum(a[k]) != 0), 0)
                if find:
                    make = [j[0] or j[1], a[find][0] or a[find][1]]
                    visited.append(find)
                    li.append(make)
            else:
                li.append(j)
    return li
