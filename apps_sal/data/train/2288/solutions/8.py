input = __import__('sys').stdin.readline
def MIS(): return map(int, input().split())


class Sandgraph:
    def __init__(_, X):
        _.z = _.x1 = 0
        _.x2 = X

    def add(_, dt):
        d1 = min(dt, X - (_.x2 + _.z - _.x1))
        _.z += d1
        dt -= d1
        d1 = min(dt, _.x2 - _.x1)
        _.z += d1
        _.x2 -= d1

    def sub(_, dt):
        d1 = min(dt, _.z)
        _.z -= d1
        dt -= d1
        d1 = min(dt, _.x2 - _.x1)
        _.x1 += d1

    def __call__(_, a):
        if a <= _.x1:
            return _.z
        elif a <= _.x2:
            return a + _.z - _.x1
        else:
            return _.x2 + _.z - _.x1


X = int(input())
k = int(input())
rev = list(MIS())
Q = int(input())
sand = Sandgraph(X)

last_t = 0
i = 0
for QUERY in range(Q):
    t, a = MIS()
    while i < k and rev[i] <= t:
        dt = rev[i] - last_t
        if i % 2 == 0:
            sand.sub(dt)
        else:
            sand.add(dt)
        last_t = rev[i]
        i += 1
    dt = t - last_t
    if i % 2 == 0:
        sand.sub(dt)
    else:
        sand.add(dt)
    print(sand(a))
    last_t = t
