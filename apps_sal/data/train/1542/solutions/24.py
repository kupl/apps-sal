def calc(W, board):
    d = t = score = 0
    for i in range(8):
        if board[i] == 'd':
            score += (2 * W[i])
        elif board[i] == 't':
            score += (3 * W[i])
        elif board[i] == 'D':
            d += 1
            score += W[i]
        elif board[i] == 'T':
            t += 1
            score += W[i]
        else:
            score += W[i]
    score *= 2**d * 3**t
    return score


def __starting_point():
    output = ""
    for test in range(int(input())):
        N = int(input())
        board = input()
        W = [int(x) for x in input().split()]
        m = -1
        for i in range(N - 7):
            m = max(m, calc(W, board[i:i + 8]))
        output += str(m) + "\n"
    print(output.rstrip())


__starting_point()
