def solve(arr):
    remove = list(set(arr))
    print(remove)
    duplicates = []
    print(arr)
    for k in range(len(remove)):
        print('K>', remove[k])
        for (i, j) in enumerate(arr):
            if j == remove[k]:
                duplicates.append(i)
                print(duplicates)
        if len(duplicates) > 1:
            for n in range(0, len(duplicates) - 1):
                arr[duplicates[n]] = ''
            duplicates = []
        else:
            duplicates = []
    while '' in arr:
        arr.remove('')
    print(arr)
    return arr
