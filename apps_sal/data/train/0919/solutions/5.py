# evens
def solve(s):
    seen = set()
    out = 0
    for c in s:
        if c in seen:
            out += len(seen) - 1
            seen = set()
        else:
            seen.add(c)
    return out + len(seen)


for tc in range(int(input())):
    input()
    s = [int(x) for x in input().strip().split(' ')]
    print(solve(s))
