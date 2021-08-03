
def solve(s, p):
    diffs = 0
    for x, y in zip(s, p):
        if x == y:
            continue
        if x == '0':
            if diffs < 1:
                return "No"
            diffs -= 1
        else:
            diffs += 1
    return "Yes" if diffs == 0 else "No"


for _ in range(int(input())):
    l = int(input())
    s = input().strip()
    p = input().strip()
    print(solve(s, p))
