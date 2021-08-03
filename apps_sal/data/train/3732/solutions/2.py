def is_madhav_array(arr):
    def check(a, n=1):
        return True if len(a) == n else sum(a[:n]) == sum(a[n:2 * n + 1]) and check(a[n:], n + 1)
    return False if len(arr) <= 1 else check(arr)
