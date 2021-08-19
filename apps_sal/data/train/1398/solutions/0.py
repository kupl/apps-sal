def solve(S):
    a = set(S)
    return len(a)


t = int(input())
for _ in range(t):
    s = input()
    print(solve(s))
