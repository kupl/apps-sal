def fibonacci(array,
              index):

    return array[index - 1] + array[index - 2]


def jacobsthal(array,
               index):

    return array[index - 1] + 2 * array[index - 2]


def padovan(array,
            index):

    return array[index - 2] + array[index - 3]


def pell(array,
         index):

    return 2 * array[index - 1] + array[index - 2]


def tetranacci(array,
               index):

    return array[index - 1] + array[index - 2] + array[index - 3] + array[index - 4]


def tribonacci(array,
               index):

    return array[index - 1] + array[index - 2] + array[index - 3]


MAP = {"fib": fibonacci,
       "jac": jacobsthal,
       "pad": padovan,
       "pel": pell,
       "tet": tetranacci,
       "tri": tribonacci}


def initialize(pattern):

    if (pattern[0] == "pad"):

        return [0,
                1,
                0,
                0]
    else:

        return [0,
                0,
                0,
                1]


def zozonacci(pattern,
              length):

    result = []
    if (not (len(pattern)
             and length)):

        return result

    result = initialize(pattern)
    if (length <= 4):

        return result[:length]

    index = 4
    while (len(result) < length):
        for sequence in pattern:
            current = MAP[sequence](result,
                                    index)
            result.append(current)
            index += 1
            if (len(result) == length):
                break

    return result
