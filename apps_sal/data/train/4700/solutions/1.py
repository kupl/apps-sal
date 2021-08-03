def solve(arr):
    result = arr[0]
    for number_array in range(1, len(arr)):
        result = [x * y for x in result for y in arr[number_array]]
    return max(result)
