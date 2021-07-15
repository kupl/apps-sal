
def find_uniq(arr):
    arr.sort(key=lambda x: x.lower())
    arr1 = [set(i.lower()) for i in arr]
    return arr[0] if arr1.count(arr1[0]) == 1 and str(arr1[0]) != 'set()' else arr[-1]
