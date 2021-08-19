try:
    t = int(input())
    result = []
    for i in range(t):
        count = 0
        li = list(map(int, input().split()))
        scores = list(map(int, input().split()))
        scores.sort(reverse=True)
        needed_score = scores[li[1] - 1]
        for u in scores:
            if u >= needed_score:
                count = count + 1
            else:
                continue
        result.append(count)
    for v in result:
        print(v)
except:
    pass
