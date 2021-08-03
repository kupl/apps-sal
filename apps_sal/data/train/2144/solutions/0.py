
def main():
    k = int(input())
    n = []
    a = []
    for i in range(k):
        line = [int(x) for x in input().split()]
        ni = line[0]
        ai = []
        n.append(ni)
        a.append(ai)
        for j in range(ni):
            ai.append(line[1 + j])
    answer, c, p = solve(k, n, a)
    if answer:
        print("Yes")
        for i in range(k):
            print(c[i], p[i] + 1)
    else:
        print("No")


def solve(k, n, a):
    asum, sums = calc_sums(k, n, a)
    if asum % k != 0:
        return False, None, None
    tsum = asum / k
    num_map = build_num_map(k, n, a)
    masks = [None] * (1 << k)
    simple = [False] * (1 << k)
    for i in range(k):
        for j in range(n[i]):
            found, mask, path = find_cycle(i, j, i, j, k, n, a, sums, tsum, num_map, 0, dict())
            if found:
                simple[mask] = True
                masks[mask] = path
    for i in range(1 << k):
        if not simple[i]:
            continue
        mask = i
        zeroes_count = 0
        for u in range(k):
            if (1 << u) > mask:
                break
            if (mask & (1 << u)) == 0:
                zeroes_count += 1
        for mask_mask in range(1 << zeroes_count):
            mask_child = 0
            c = 0
            for u in range(k):
                if (1 << u) > mask:
                    break
                if (mask & (1 << u)) == 0:
                    if (mask_mask & (1 << c)) != 0:
                        mask_child = mask_child | (1 << u)
                    c += 1
            if masks[mask_child] and not masks[mask_child | mask]:
                masks[mask_child | mask] = {**masks[mask_child], **masks[mask]}
                if (mask_child | mask) == ((1 << k) - 1):
                    c = [-1] * k
                    p = [-1] * k
                    d = masks[(1 << k) - 1]
                    for key, val in list(d.items()):
                        c[key] = val[0]
                        p[key] = val[1]
                    return True, c, p
    if masks[(1 << k) - 1]:
        c = [-1] * k
        p = [-1] * k
        d = masks[(1 << k) - 1]
        for key, val in list(d.items()):
            c[key] = val[0]
            p[key] = val[1]
        return True, c, p
    return False, None, None


def build_num_map(k, n, a):
    result = dict()
    for i in range(k):
        for j in range(n[i]):
            result[a[i][j]] = (i, j)
    return result


def find_cycle(i_origin, j_origin, i, j, k, n, a, sums, tsum, num_map, mask, path):
    if (mask & (1 << i)) != 0:
        if i == i_origin and j == j_origin:
            return True, mask, path
        else:
            return False, None, None
    mask = mask | (1 << i)
    a_needed = tsum - (sums[i] - a[i][j])
    if a_needed not in num_map:
        return False, None, None
    i_next, j_next = num_map[a_needed]
    path[i_next] = (a[i_next][j_next], i)
    return find_cycle(i_origin, j_origin, i_next, j_next, k, n, a, sums, tsum, num_map, mask, path)


def calc_sums(k, n, a):
    sums = [0] * k
    for i in range(k):
        for j in range(n[i]):
            sums[i] = sums[i] + a[i][j]
    asum = 0
    for i in range(k):
        asum = asum + sums[i]
    return asum, sums


def __starting_point():
    main()


__starting_point()
