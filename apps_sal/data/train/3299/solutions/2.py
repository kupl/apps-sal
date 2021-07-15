from collections import deque, defaultdict

def calc(cards):
    memo = defaultdict(int)
    ans = 0
    q = deque([(1, 0, tuple(cards))])
    while q:
        i, score, remains = q.popleft()
        if len(remains) == 1:
            score += remains[0] * 2 ** i
            if score > ans:
                ans = score
        else:
            score_l = score + (remains[0] * 2 ** i)
            if score_l > memo[remains[1:]]:
                memo[remains[1:]] = score_l
                q.append((i + 1, score_l, remains[1:]))
            score_r = score + (remains[-1] * 2 ** i)
            if score_r > memo[remains[:-1]]:
                memo[remains[:-1]] = score_r
                q.append((i + 1, score_r, remains[:-1]))
    return ans
