import sys
input = sys.stdin.readline


def inint():
    return(int(input()))


def inlst():
    return(list(map(int, input().split())))


def instr():
    s = input()
    return(list(s[:len(s) - 1]))


def invar():
    return(list(map(int, input().split())))


def isOdd(num):
    return (num & 1) == 1


n, m = invar()

tree = [{'round_num': m, 'winner': -1} for _ in range(2 * n + 1, 0, -1)]


def modify(left, right, pair):
    left += n
    right += n
    while left <= right:
        if isOdd(left):
            tree[left] = pair

        if not isOdd(right):
            tree[right] = pair

        left = int((left + 1) / 2)
        right = int((right - 1) / 2)


def query(pos):
    pos += n
    min = 1000000
    winner = -1
    while pos > 0:
        if tree[pos]['round_num'] < min:
            winner = tree[pos]['winner']
            min = tree[pos]['round_num']

        pos >>= 1

    return winner + 1 if winner > -1 else 0


rounds = []
for _ in range(m):
    li, ri, xi = invar()
    rounds.append({'left': li - 1, 'right': ri - 1, 'winner': xi - 1})

for idx in range(m - 1, -1, -1):
    round = rounds[idx]
    if round['winner'] > 0:
        modify(round['left'], round['winner'] - 1, {'round_num': idx, 'winner': round['winner']})
    if round['winner'] < n:
        modify(round['winner'] + 1, round['right'], {'round_num': idx, 'winner': round['winner']})

print(*[query(i) for i in range(n)])
