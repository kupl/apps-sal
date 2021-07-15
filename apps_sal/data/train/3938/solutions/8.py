def sorted_brands(arr):
    arr = [k['brand'] for k in arr]
    return sorted(set(arr), key=lambda x: (-arr.count(x), arr.index(x)))
