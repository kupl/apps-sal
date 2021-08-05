T = int(input())
for _ in range(T):
    n, p = tuple(map(int, input().split(' ')))
    solved_by = list(map(int, input().split(' ')))
    cakewalk, hard = (0, 0)
    for x in solved_by:
        if x >= p // 2:
            cakewalk = cakewalk + 1
        elif x <= p // 10:
            hard = hard + 1
    if cakewalk == 1 and hard == 2:
        print('yes')
    else:
        print('no')
