def solve(arr):
    while 1:
        number = arr[0]
        opposite_number = number * (-1)
        if opposite_number in arr:
            arr.remove(number)
            arr.remove(opposite_number)
        else:
            return arr[0]
