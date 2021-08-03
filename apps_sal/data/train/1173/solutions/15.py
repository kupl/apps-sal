# cook your dish here
test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    seq = list(map(int, input().split()))

    triplets = 0
    res = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        res[i] = res[i - 1] ^ seq[i - 1]

    xors = {}
    for i in range(n + 1):
        if res[i] not in xors:
            xors[res[i]] = [i]
        else:
            xors[res[i]].append(i)

    # print(xors)
    for key in xors.keys():
        if len(xors[key]) > 1:
            for i in range(len(xors[key]) - 1):
                for j in range(i + 1, len(xors[key])):
                    triplets += int(xors[key][j] - xors[key][i] - 1)
    print(triplets)
