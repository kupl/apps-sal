N, L = map(int, input().split())
S = [input() for i in range(N)]

S_sorted = sorted(S)
Word = ''.join(S_sorted)

print(Word)
