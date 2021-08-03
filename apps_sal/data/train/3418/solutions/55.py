def reverse_list(l):

    # =============================================================================
    #     This function reverses the order of items in a given list.  If the given
    #     list is empty, the function returns an empty list
    #
    #     Example:
    #        reverse_list([1,2,3,4]) ==> [4,3,2,1]
    # =============================================================================

    result = []

    if len(l) == 0:
        return result

    for item in l[::-1]:
        result.append(item)

    return (result)
