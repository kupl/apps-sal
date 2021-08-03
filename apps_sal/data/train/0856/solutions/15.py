for _ in range(int(input())):
    n = int(input())
    D = dict()
    for i in range(n):
        word, tp = map(str, input().split())
        tp = int(tp)

        if tp == 1:
            if D.get(word, 0) != 0:
                D[word][0] += 1
            else:
                D[word] = [1, 0]
        else:
            if D.get(word, 0) != 0:
                D[word][1] += 1
            else:
                D[word] = [0, 1]
    max_select = 0
    for a, b in D.values():
        max_select += max(a, b)
    print(max_select)
