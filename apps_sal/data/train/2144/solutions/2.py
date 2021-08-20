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
    (answer, c, p) = solve(k, n, a)
    if answer:
        print('Yes')
        for i in range(k):
            print(c[i], p[i] + 1)
    else:
        print('No')


def solve(k, n, a):
    (asum, sums) = calc_sums(k, n, a)
    if asum % k != 0:
        return (False, None, None)
    tsum = asum / k
    num_map = build_num_map(k, n, a)
    masks = [None] * (1 << k)
    simple = [False] * (1 << k)
    answer = [False] * (1 << k)
    left = [0] * (1 << k)
    right = [0] * (1 << k)
    by_last_one = [[] for _ in range(k)]
    for i in range(k):
        for j in range(n[i]):
            (found, mask, path) = find_cycle(i, j, i, j, k, n, a, sums, tsum, num_map, 0, [])
            if found and (not answer[mask]):
                answer[mask] = True
                masks[mask] = path
                simple[mask] = True
                by_last_one[calc_last_one(mask)].append(mask)
    if answer[(1 << k) - 1]:
        return build_answer(k, masks, left, right)
    for mask_right in range(2, 1 << k):
        if not simple[mask_right]:
            continue
        last_one = calc_last_one(mask_right)
        zeroes_count = 0
        alternative_sum = 0
        zero_list = []
        for u in range(last_one):
            if mask_right & 1 << u == 0:
                zeroes_count += 1
                alternative_sum += len(by_last_one[u])
                zero_list.append(u)
        if zeroes_count == 0:
            continue
        if alternative_sum < 1 << zeroes_count:
            for fill_last_zero in zero_list:
                for mask_left in by_last_one[fill_last_zero]:
                    if mask_left & mask_right != 0:
                        continue
                    joint_mask = mask_left | mask_right
                    if not answer[joint_mask]:
                        answer[joint_mask] = True
                        left[joint_mask] = mask_left
                        right[joint_mask] = mask_right
                        by_last_one[last_one].append(joint_mask)
                        if joint_mask == (1 << k) - 1:
                            return build_answer(k, masks, left, right)
        else:
            for mask_mask in range(1 << zeroes_count):
                mask_left = 0
                for u in range(zeroes_count):
                    if mask_mask & 1 << u != 0:
                        mask_left = mask_left | 1 << zero_list[u]
                joint_mask = mask_left | mask_right
                if answer[mask_left] and (not answer[joint_mask]):
                    answer[joint_mask] = True
                    left[joint_mask] = mask_left
                    right[joint_mask] = mask_right
                    by_last_one[last_one].append(joint_mask)
                    if joint_mask == (1 << k) - 1:
                        return build_answer(k, masks, left, right)
    return (False, None, None)


def calc_last_one(x):
    result = -1
    while x > 0:
        x = x >> 1
        result = result + 1
    return result


def build_answer(k, masks, left, right):
    c = [-1] * k
    p = [-1] * k
    pos = (1 << k) - 1
    while not masks[pos]:
        for (i, a, j) in masks[right[pos]]:
            c[i] = a
            p[i] = j
        pos = left[pos]
    for (i, a, j) in masks[pos]:
        c[i] = a
        p[i] = j
    return (True, c, p)


def build_num_map(k, n, a):
    result = dict()
    for i in range(k):
        for j in range(n[i]):
            result[a[i][j]] = (i, j)
    return result


def find_cycle(i_origin, j_origin, i, j, k, n, a, sums, tsum, num_map, mask, path):
    if mask & 1 << i != 0:
        if i == i_origin and j == j_origin:
            return (True, mask, path)
        else:
            return (False, None, None)
    mask = mask | 1 << i
    a_needed = tsum - (sums[i] - a[i][j])
    if a_needed not in num_map:
        return (False, None, None)
    (i_next, j_next) = num_map[a_needed]
    path.append((i_next, a[i_next][j_next], i))
    return find_cycle(i_origin, j_origin, i_next, j_next, k, n, a, sums, tsum, num_map, mask, path)


def calc_sums(k, n, a):
    sums = [0] * k
    for i in range(k):
        for j in range(n[i]):
            sums[i] = sums[i] + a[i][j]
    asum = 0
    for i in range(k):
        asum = asum + sums[i]
    return (asum, sums)


def __starting_point():
    main()


__starting_point()
