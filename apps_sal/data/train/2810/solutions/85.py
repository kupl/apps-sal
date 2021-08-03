def solve(arr):
    # return the number of letters that occupy their positions inthe alphabet
    # create alphabet list
    alpha = [chr(i) for i in range(ord('a'), ord('z') + 1, 1)]
    lst = []
    for item in arr:  # have to compare them in the same case
        lst.append(sum([x.lower() == y.lower() for (x, y) in zip(alpha, item)]))
    return lst
