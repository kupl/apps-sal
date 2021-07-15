def solve(n,
          k):

    result = {}
    index, start, end = 0, 0, n - 1
    while (start <= end):
        result[end] = index
        index += 1
        if (start != end):
            result[start] = index

        index += 1
        start += 1
        end -= 1

    return result[k]

