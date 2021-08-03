import sys

for __ in range(eval(input())):
    n = eval(input())
    lists = list(map(str, sys.stdin.readline().split()))
    lists.sort(key=lambda x: len(x))
    stem, stems = lists[0], []
    for k in range(len(lists[0])):
        for j in range(k + 1, len(lists[0])):
            ctr = 0
            for i in lists[1:]:
                if stem[k:j + 1] in i:
                    ctr += 1
            if ctr == n - 1:
                stems.append(stem[k:j + 1])

    stems.sort(key=lambda x: len(x), reverse=True)
    stems = [x for x in stems if len(x) == len(stems[0])]
    stems.sort()
    print(stems[0] if len(stems) > 0 else "")
