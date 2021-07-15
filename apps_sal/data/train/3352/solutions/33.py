def find_longest(arr):
    box = []
    base = 0
    for i,x in enumerate(arr):
        for j in str(x):
            box.append(j)
            if len(box) > base:
                base = len(box)
                result = i
        box.clear()
    return arr[result]
