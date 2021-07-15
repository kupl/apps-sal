def util(x1, x2, y1, y2):
    d = x1 - y1
    n = x2 - y2
    if d and not n%d:
        return n//d
    return 1

def solve(p, q, r, a, b, c, res=0):
    if p == a and q == b and r == c:
        return res
    if res >= 2:
        return 3
    adds = [a-p, b-q, c-r]
    muls = []
    if p and not a%p:
        muls += [a//p]
    if q and not b%q:
        muls += [b//q]
    if r and not c%r:
        muls += [c//r]
    muls.append(util(p, a, q, b))
    muls.append(util(p, a, r, c))
    muls.append(util(q, b, r, c))
    mask = 2**3
    ans = 3
    for msk in range(1, mask):
        for add in adds:
            np, nq, nr = p, q, r
            if msk & 1:
                np += add
            if msk & 2:
                nq += add
            if msk & 4:
                nr += add
            ans = min(ans, solve(np, nq, nr, a, b, c, res+1))
        for mul in muls:
            np, nq, nr = p, q, r
            if msk & 1:
                np *= mul
            if msk & 2:
                nq *= mul
            if msk & 4:
                nr *= mul
            ans = min(ans, solve(np, nq, nr, a, b, c, res+1))
    return ans

def main():
    t = int(input())
    for i in range(t):
        p, q, r = map(int, input().split())
        a, b, c = map(int, input().split())
        print(solve(p, q, r, a, b, c))

def __starting_point():
    main()

__starting_point()
