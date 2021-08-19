def p_input():
    tot = int(input())
    dicts = []
    for i in range(tot):
        n = [int(x) for (j, x) in enumerate(input().split()) if j < 2]
        dicts = input().split()[:n[0]]
        sents = []
        for _ in range(n[1]):
            sent = input().split()
            sents += sent[1:int(sent[0]) + 1]
        print(' '.join(('YES' if x in sents else 'NO' for x in dicts)))


def __starting_point():
    p_input()


__starting_point()
