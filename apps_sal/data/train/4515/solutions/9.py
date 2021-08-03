def diff(arr):
    if not arr:
        return False

    def cust_key(s):
        a, b = map(int, s.split("-"))
        return abs(a - b)
    m = max(arr, key=cust_key)
    return m if len(set(m.split("-"))) == 2 else False
