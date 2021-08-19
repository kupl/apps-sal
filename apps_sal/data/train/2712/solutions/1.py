def loneliest(n):

    def loneliness(it):
        (i, v) = it
        return (sum(lst[max(0, i - v):i + v + 1]) - v, abs(v - 1))
    lst = list(map(int, str(n)))
    return 1 in lst and 1 == min(enumerate(lst), key=loneliness)[1]
