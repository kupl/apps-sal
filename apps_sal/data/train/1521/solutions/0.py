from operator import itemgetter
t = int(input())
for _ in range(t):
    n = int(input())
    start = []
    end = []
    for i in range(n):
        first, last = map(int, input().split())
        start.append((first, i))
        end.append((last, i))
    score = [0] * n
    start.sort(key=itemgetter(0))
    end.sort(key=itemgetter(0), reverse=True)
    for i in range(n - 1):
        score[start[i][1]] += n - i - 1
        score[end[i][1]] += n - i - 1
    print(' '.join([str(i) for i in score]))
