def solve(S):
    i = 0
    count = 0
    L = 0
    n = len(S)
    end = False
    size = 0
    while i < n:
        if S[i] == '.':
            size += 1
        elif size != 0:
            if size > L:
                count += 1
                L = size
            size = 0
        i += 1
    return count


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
