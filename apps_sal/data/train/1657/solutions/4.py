def string_func(s, n):
    (m, table) = (len(s), {})
    for i in range(m):
        if i not in table:
            (j, cycle) = (i, [])
            while i != j or not cycle:
                cycle.append(j)
                j = min(2 * j + 1, 2 * (m - j - 1))
            table.update(zip(cycle[n % len(cycle):] + cycle, cycle))
    return ''.join((s[table[i]] for i in range(m)))
