def find_longest(arr):
    arr = [str(i) for i in arr]

    def m_len(x):
        return len(x)
    return int(max(arr, key=m_len))
