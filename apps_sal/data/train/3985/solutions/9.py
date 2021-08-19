def find_even_index(arr):

    def partial_sum(arr):
        total = 0
        for i in arr:
            total += i
            yield total
    sums = list(partial_sum(arr))

    def sumleft(i):
        if i != 0:
            return sums[i - 1]
        else:
            return 0

    def sumright(i):
        return sums[len(sums) - 1] - sums[i]
    for i in range(len(arr)):
        sl = sumleft(i)
        sr = sumright(i)
        if sl == sr:
            return i
    return -1
