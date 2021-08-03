def solve(arr):

    # =============================================================================
    #     This function removes the left-most duplicates from a list of integers and
    #     returns the result.
    #
    #     Example:
    #         Remove the 3's at indices 0 and 3
    #         followed by removing a 4 at index 1
    #         solve([3, 4, 4, 3, 6, 3]) # => [4, 6, 3]
    # =============================================================================

    print(arr)

    arr.reverse()

    print(arr)

    result = []

    for item in arr:
        if item not in result:
            result.append(item)

    result.reverse()

    return result
