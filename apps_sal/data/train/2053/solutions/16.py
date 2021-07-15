import bisect

def party_sweet(b, g):
    maxb = max(b)
    ming = min(g)
    if maxb > ming:
        return -1
    elif maxb == ming:
        return (sum(b) - maxb)* len(g) + sum(g)
    else:
        return (sum(b))* len(g) + sum(g) - maxb * (len(g) - 1) - sorted(b)[-2]



def main():
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    g = list(map(int, input().split()))

    print(party_sweet(b, g))

def __starting_point():
    main()
__starting_point()
