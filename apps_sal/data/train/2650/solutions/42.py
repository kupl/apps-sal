(n, l) = map(int, input().split())
words = [input() for i in range(n)]
words = list(sorted(words))
s = ''
for i in range(n):
    s += words[i]
print(s)
