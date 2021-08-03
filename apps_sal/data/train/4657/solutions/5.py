def sort_by_perfsq(arr):

    def get_pos_nums(digs, currn=''):
        if len(digs) == 1:
            nums.append(currn + digs[0])

        for d in digs:
            locd = digs[:]
            locd.remove(d)
            get_pos_nums(locd, currn + d)

    count_sq = []

    for x in arr:
        count_sq.append([x, 0])

        digs = [d for d in str(x)]
        nums = []
        get_pos_nums(digs)
        nums = set(map(int, nums))

        for n in nums:
            if n ** 0.5 % 1 == 0:
                count_sq[-1][1] += 1

    count_sq.sort()
    count_sq.sort(key=lambda num: num[1], reverse=True)
    return [num[0] for num in count_sq]
