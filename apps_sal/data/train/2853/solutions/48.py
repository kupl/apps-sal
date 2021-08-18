def solve(arr):

    print(arr)

    arr.reverse()

    print(arr)

    result = []

    for item in arr:
        if item not in result:
            result.append(item)

    result.reverse()

    return result
