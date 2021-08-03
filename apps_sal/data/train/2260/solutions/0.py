import random
import math


def set_color(game, color):
    color_count[game[0]][game[2]] -= 1
    color_count[game[1]][game[2]] -= 1
    game[2] = color
    color_count[game[0]][game[2]] += 1
    color_count[game[1]][game[2]] += 1


def fix(node):
    minimum = math.inf
    maximum = 0

    for i in range(k):
        minimum = min(minimum, color_count[node][i])
        maximum = max(maximum, color_count[node][i])

    if maximum - minimum <= 2:
        return False

    rand = 0
    for game in games:
        if (game[0] == node or game[1] == node) and color_count[node][game[2]] == maximum:
            rand = r(1, k)
            set_color(game, rand % k)
            return True

    return False


n, m, k = list(map(int, input().split()))
games = [[0 for _ in range(4)] for _ in range(m)]
color_count = [[0 for _ in range(k)] for _ in range(n)]
answers = [0 for _ in range(m)]
_ = list(map(int, input().split()))

color = 0
def r(x, y): return random.randint(x, y)


for i in range(m):
    a, b = list(map(int, input().split()))
    color = r(1, k) % k
    games[i] = [a - 1, b - 1, color, i]
    color_count[games[i][0]][color] += 1
    color_count[games[i][1]][color] += 1

bad = True

while bad:
    random.shuffle(games)
    bad = False

    for i in range(n):
        while(fix(i)):
            bad = True

for game in games:
    answers[game[3]] = game[2] + 1

for i in range(m):
    print(answers[i])
