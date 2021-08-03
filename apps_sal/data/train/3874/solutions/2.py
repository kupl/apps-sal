def sort_twisted37(arr):
    def twisted(n): return int(''.join('3' if c == '7' else '7' if c == '3' else c for c in str(n)))
    return sorted(arr, key=twisted)
