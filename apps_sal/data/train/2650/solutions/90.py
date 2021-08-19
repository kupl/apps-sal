(N, L) = map(int, input().split())
word_list = [input() for i in range(N)]
word_list.sort()
for i in word_list:
    print(i, end='')
print()
