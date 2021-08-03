t = int(input())
for i in range(t):
    N = int(input())
    word = input()
    hit = [0] * N
    for x in range(N):
        if word[x] == '1':
            hit[x] = 1
            if x > 0:
                hit[x - 1] = 1
            if x < N - 1:
                hit[x + 1] = 1
    print(hit.count(0))
