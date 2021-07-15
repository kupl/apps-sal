def unflatten(flat_array, depth):
    right = True
    length = len(flat_array)
    for _ in range(depth):
        flat_array = unflatten_helper(flat_array, right)
        right = not right
    return flat_array
        
        
def unflatten_helper(arr, right):
    newArr = []
    length = len(arr)
    if right:
        i = 0
        while i < length:
            if isinstance(arr[i], list):
                newArr.append(unflatten_helper(arr[i], right))
                i += 1
            else:
                rem = arr[i] % (length - i)
                if rem > 2:
                    newArr.append(arr[i:rem+i])
                    i += rem
                else:
                    newArr.append(arr[i])
                    i += 1
    else:
        i = length - 1
        while i >= 0:
            if isinstance(arr[i], list):
                newArr.append(unflatten_helper(arr[i], right))
                i -= 1
            else:
                rem = arr[i] % (i + 1)
                if rem > 2:
                    newArr.append(arr[i-rem+1:i+1])
                    i -= rem
                else:
                    newArr.append(arr[i])
                    i -= 1
        newArr = newArr[::-1]
    return newArr

