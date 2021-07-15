def find_longest(arr):
    return [i for i in arr if len(str(i)) == len(str(max(arr)))][0]
