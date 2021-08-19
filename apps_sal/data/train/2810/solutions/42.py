def solve(arr):

    def f(x):
        return sum([1 for i in range(len(x)) if ord(x[i].lower()) - 97 == i])
    return [f(i) for i in arr]
