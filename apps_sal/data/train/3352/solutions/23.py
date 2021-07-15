def find_longest(arr):
    return int(max([str(number) for number in arr],key=len))
