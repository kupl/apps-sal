def diff(arr):
    diff = []
    if arr == []:
        return False
    for i in range(len(arr)):
        str = arr[i].split('-')
        diff.append(abs(int(str[1]) - int(str[0])))
    if max(diff) == 0:
        return False
    for j in range(len(arr)):
        if diff[j] == max(diff):
            return arr[j]
