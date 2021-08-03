def find_all(sum_dig, digs):
    def rec(ds=digs, min_dig=1, sum_prev=0):
        for i in range(min_dig, 10):
            sum_cur = sum_prev + i
            if ds == 1:
                if sum_cur == sum_dig:
                    yield str(i)
            elif sum_cur < sum_dig:
                for r in rec(ds - 1, i, sum_cur):
                    yield str(i) + r
    results = [int(s) for s in rec()]
    return [len(results), min(results), max(results)] if results else []
