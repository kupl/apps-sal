def __starting_point():
    (st_num, sb_num) = list(map(int, input().strip().split()))
    scores = []
    for _ in range(sb_num):
        scores.append(list(map(float, input().strip().split())))
    for el in zip(*scores):
        print(sum(el) / sb_num)


__starting_point()
