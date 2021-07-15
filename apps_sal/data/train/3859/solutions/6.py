def odd_one(arr):
    for num in arr:
        if num % 2 != 0:
            return arr.index(num)
            break
    else: 
        return -1

