def find_missing_numbers(arr):
    try:
        return [i for i in range(arr[0],arr[len(arr)-1]) if i not in arr]
    except IndexError:
        return []
