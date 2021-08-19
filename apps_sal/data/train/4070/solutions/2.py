def magic_sum(arr):

    def check(x):
        return x % 2 and '3' in str(x)
    return sum((x for x in arr if check(x))) if arr else 0
