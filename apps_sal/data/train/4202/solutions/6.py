def ulam_sequence(u0, u1, n):
    """
    Input
    u0 = first number
    u1 = second numberr
    n  = number of elements in sequence

    Return
    Ulam Sequence (u0, u1, u2...) with n-terms
    """
    U = [u0, u1]
    next_num = u1 + 1
    while len(U) < n:
        count = 0
        index = 0
        for number in U:
            if next_num - number in U and number != next_num / 2:
                count += 1
            if count >= 3:
                break
        if count < 3 and count > 0:
            U.append(next_num)
        next_num += 1
    return U
