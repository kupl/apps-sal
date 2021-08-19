import sys


def solve(N: int, T: int, A: 'List[int]'):
    right_max = [0] * N
    m_a = 0
    for i in range(1, N):
        m_a = max(m_a, A[-i])
        right_max[-i - 1] = m_a
    m_p = 0
    count = 0
    for (i, a) in enumerate(A):
        profit = right_max[i] - a
        if profit > m_p:
            m_p = profit
            count = 1
        elif profit == m_p:
            count += 1
    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))
    T = int(next(tokens))
    A = [int(next(tokens)) for _ in range(N)]
    solve(N, T, A)


def __starting_point():
    main()


__starting_point()
