def find_missing_number(sq):
    num = 0
    sq = sq.split()
    try:
        sq = list(map(int, sq))
        sq = sorted(sq)
        for i in sq:
            num += 1
            if i != num:
                return num
        return 0
    except ValueError:
        return 1
