(N, L) = map(int, input().split())
word = []
count = 0
while N > count:
    S = input()
    word.append(S)
    count += 1
word = sorted(word)
ans = ''.join(word)
print(ans)
