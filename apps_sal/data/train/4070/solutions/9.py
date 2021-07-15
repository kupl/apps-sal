def magic_sum(arr):
    if arr == None or arr == []:
        return 0
    output = 0
    for num in arr:
        if '3' in str(num) and num % 2 == 1:
            output += num
        else:
            pass
    return output
