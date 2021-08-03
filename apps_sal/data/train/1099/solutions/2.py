t = int(input())
for i in range(t):
    n = int(input())
    scores = {}
    for j in range(n):
        line = input()
        (key, value) = line.split(' ')
        if value == '+':
            scores[key] = 1
        else:
            scores[key] = -1
    sum = 0
    for k in scores:
        sum += scores[k]
    print(sum)
