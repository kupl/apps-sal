def sum_array(arr):

    def sum_array_(x):
        return sum(x) - min(x) - max(x) * bool(x[1:])
    return sum_array_(arr or [0])
