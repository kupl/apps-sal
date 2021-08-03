def calculate_array(array,
                    exponent):

    result = 0
    for i in range(len(array)):
        result += (array[i] ** exponent)

    return result


def array_madness(a,
                  b):

    sum_a, sum_b = calculate_array(a, 2), calculate_array(b, 3)
    if (sum_b < sum_a):

        return True

    return False
