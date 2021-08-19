def even_numbers(arr, n):

    # =============================================================================
    #     This function given an array of digital numbers, returns a new array of
    #     length n containing the last even numbers from the original array
    #     (in the same order).
    #
    #     The original array will be not empty and will contain at least "n"
    #     even numbers.
    #
    #     Example:
    #         ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) ==> [4, 6, 8]
    #         ([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) ==> [-8, 26]
    #         ([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) ==> [6]
    # =============================================================================

    result = []

    myList = arr
    evensList = [x for x in myList if x % 2 == 0]  # extract even nums from arr

    evensList = evensList[::-1]

    for i in range(0, n):

        result.append(evensList[i])

    return result[::-1]
