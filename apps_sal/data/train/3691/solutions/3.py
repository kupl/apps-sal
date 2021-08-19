result = ['1']


def get_a_down_arrow_of(n):
    while len(result) < n:
        i = len(result)
        result.append(result[-1][:i] + str((i + 1) % 10) + result[-1][i - 1::-1])
    return '\n'.join((result[x].center(2 * n - 1).rstrip() for x in range(n - 1, -1, -1)))
