def find_longest(arr):
    list1 = []
    for i in arr:
        x = str(i)
        z = len(x)
        list1.append(z)
        y = list1.index(max(list1))
    return arr[y]
