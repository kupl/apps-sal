def main():
    from bisect import bisect
    n, A, cf, cm, m = list(map(int, input().split()))
    skills = list(map(int, input().split()))
    xlat = sorted(list(range(n)), key=skills.__getitem__)
    sorted_skills = [skills[_] for _ in xlat]
    bottom_lift, a, c = [], 0, 0
    for i, b in enumerate(sorted_skills):
        c += i * (b - a)
        bottom_lift.append(c)
        a = b
    root_lift, a = [0], 0
    for b in reversed(sorted_skills):
        a += A - b
        root_lift.append(a)
    max_level = -1
    for A_width, a in enumerate(root_lift):
        if m < a:
            break
        money_left = m - a
        floor_width = bisect(bottom_lift, money_left)
        if floor_width > n - A_width:
            floor_width = n - A_width
        money_left -= bottom_lift[floor_width - 1]
        if floor_width > 0:
            floor = sorted_skills[floor_width - 1] + money_left // floor_width
            if floor > A:
                floor = A
        else:
            floor = A
        level = cf * A_width + cm * floor
        if max_level < level:
            max_level, save = level, (A_width, floor, floor_width)
    A_width, floor, floor_width = save
    for id in xlat[:floor_width]:
        skills[id] = floor
    for id in xlat[n - A_width:]:
        skills[id] = A
    print(max_level)
    print(' '.join(map(str, skills)))


def __starting_point():
    main()

__starting_point()
