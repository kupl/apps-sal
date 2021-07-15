odd = lambda x: x&1

def is_odd_heavy(arr):
    it = iter(sorted(arr))
    return any(map(odd, it)) and all(map(odd, it))
