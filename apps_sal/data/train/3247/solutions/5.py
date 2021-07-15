def sort_by_height(arr):
    s=sorted(n for n in arr if n!=-1)
    return [n if n==-1 else s.pop(0) for n in arr]
