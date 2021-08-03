def solve(n):
    b = [int(str(n)[0]) - 1] + [9 for x in str(n)[1:]]
    digsum = sum(b)
    if digsum <= sum([int(x) for x in str(n)]):
        return n
    for i in range(len(str(n)) - 1, -1, -1):
        a = [int(x) for x in str(n)[:i]] + [int(str(n)[i]) - 1] + [9 for x in str(n)[i + 1:]]
        print((i, a))
        if sum(a) == digsum:
            break
    return int("".join([str(x) for x in a]))
