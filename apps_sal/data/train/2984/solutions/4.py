def infected_zeroes(a):
    zeros = [i for i, n in enumerate(a) if not n]
    return len(zeros) and max((y - x) // 2 for x, y in
            zip([-1 - zeros[0]] + zeros, zeros + [2*len(a) -1 - zeros[-1]]))
