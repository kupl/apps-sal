input()
def f(l):
    c = [0]*len(l)
    c[0] = c[len(c) - 1] = 9999999
    for item in range(1, len(l) - 1):
        c[item] = min(item, l[item], c[item - 1] + 1)
    for item in reversed(list(range(1, len(l) - 1))):
        c[item] = min(c[item], len(l) - 2 + 1 - item, c[item + 1] + 1)

    return max(c[1:-1])

print(f([0] + list(map(int, input().split())) + [0]))


