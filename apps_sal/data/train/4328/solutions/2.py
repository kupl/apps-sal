def friend_find(arr):
    return sum([1 for i in range(len(arr)) if arr[i] == 'red' if i > 1 and arr[i - 1] == 'blue' and (arr[i - 2] == 'blue') or (i > 0 and i < len(arr) - 1 and (arr[i - 1] == 'blue') and (arr[i + 1] == 'blue')) or (i < len(arr) - 2 and arr[i + 1] == 'blue' and (arr[i + 2] == 'blue'))])
