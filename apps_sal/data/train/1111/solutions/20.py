# cook your dish here
# BUTTON PAIRS

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    cnte = 0
    cnto = 0

    for i in l:
        if i % 2 == 0:
            cnte += 1
        else:
            cnto += 1

    res = cnte * cnto
    print(res)
