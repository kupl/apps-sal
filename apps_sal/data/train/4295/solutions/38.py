def balanced_num(number):
    if number < 10:
        return "Balanced"
    arr = [int(i) for i in str(number)]
    n = len(arr)
    if n % 2:
        if sum(arr[:len(arr)//2]) == sum(arr[len(arr)//2+1:]):
            return "Balanced"
        return "Not Balanced"
    else:
        if sum(arr[:len(arr)//2-1]) == sum(arr[len(arr)//2+1:]):
            return "Balanced"
        return "Not Balanced"
