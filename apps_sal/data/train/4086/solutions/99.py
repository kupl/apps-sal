def first_non_consecutive(arr):
    for num in arr:
        i = arr.index(num)
        if i > (len(arr) - 2):
            return None
        elif arr[i + 1] == int(num + 1):
            continue
        else:
            return arr[i + 1]
    #your code here

