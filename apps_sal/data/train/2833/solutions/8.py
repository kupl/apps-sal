def sect_sort(arr, s, l=None):
    return (lambda l: arr[:s] + sorted(arr[s:s + l]) + arr[s + l:])(len(arr) if not l else l)
