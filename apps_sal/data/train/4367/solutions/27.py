def area_or_perimeter(l, w):

    # =============================================================================
    #     This function is given the length and width of a 4-sided polygon.
    #     The polygon can either be a rectangle or a square.
    #     Note:
    #         for the purposes of this kata you will assume that it is a square
    #         if its length and width are equal, otherwise it is a rectangle.
    #
    #     If it is a square, the function returns its area. If it is a rectangle,
    #     the function returns its perimeter.
    #
    #     Examples:
    #         area_or_perimeter(6, 10) --> 32
    #         area_or_perimeter(4, 4) --> 16
    # =============================================================================

    if l == w:  # test for a square
        return (l * w)
    else:
        return ((2 * l) + (2 * w))
