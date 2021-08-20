t = int(input())
for _ in range(t):
    best = ''
    n = int(input())
    words = input().split()
    min = 20
    min_index = 0
    for (i, word) in enumerate(words):
        if len(word) < min:
            min = len(word)
            min_index = i
    for i in range(min, 0, -1):
        found = False
        for j in range(min - i + 1):
            all = True
            sub = words[min_index][j:j + i]
            for word in words:
                if sub not in word:
                    all = False
                    break
            if all:
                if best == '' or best > sub:
                    best = sub
                    found = True
        if found:
            break
    print(best)
