def isaban(i, j, ki, kj):
    if i < 0 or i > 7 or j < 0 or j > 7:
        return True
    if ki - 2 < i and i < ki + 2 and kj - 2 < j and j < kj + 2:
        return True
    return False


def ischeck(i, j, ki, kj, ai, aj):
    if i == ai and j == aj:
        return False
    if i == ai:
        if ai != ki or (kj < j and kj < aj) or (kj > j and kj > aj):
            return True
    if j == aj:
        if aj != kj or (ki < i and ki < ai) or (ki > i and ki > ai):
            return True
    if i + j == ai + aj:
        if ai + aj != ki + kj or (ki < i and ki < ai) or (ki > i and ki > ai):
            return True
    if i - j == ai - aj:
        if ai - aj != ki - kj or (ki < i and ki < ai) or (ki > i and ki > ai):
            return True
    Knight = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    for item in Knight:
        if ai == i + item[0] and aj == j + item[1]:
            return True
    return False


def ismate(i, j, ki, kj, ai, aj):
    if i == ai and j == aj:
        return False
    move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for item in move:
        ti, tj = i + item[0], j + item[1]
        if not isaban(ti, tj, ki, kj):
            if ti == ai and tj == aj:
                return False
            if not ischeck(ti, tj, ki, kj, ai, aj):
                return False
    return True


def amazon_check_mate(king, amazon):
    ki, kj = (ord(king[0]) - ord('a'), int(king[1]) - 1)
    ai, aj = (ord(amazon[0]) - ord('a'), int(amazon[1]) - 1)
    ans = [0, 0, 0, 0]
    for i in range(8):
        for j in range(8):
            if not isaban(i, j, ki, kj):
                if ischeck(i, j, ki, kj, ai, aj):
                    if ismate(i, j, ki, kj, ai, aj):
                        if i != ai or j != aj:
                            ans[0] += 1
                    else:
                        ans[1] += 1
                else:
                    if ismate(i, j, ki, kj, ai, aj):
                        ans[2] += 1
                    else:
                        ans[3] += 1
    if not isaban(ai, aj, ki, kj):
        ans[3] -= 1
    return ans
