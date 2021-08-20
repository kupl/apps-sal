import math
T = int(input())
for _ in range(T):
    word = input().split()
    N = int(word[0])
    Q = int(word[1])
    answer = 0
    answer += round(N + Q - N / (Q + 1), 15)
    print(answer)
