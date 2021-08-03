t = eval(input())
for _ in range(t):
    i, j = list(map(int, input().split()))
    bi = bin(i)[2:]
    bj = bin(j)[2:]
    k = 0
    while k < (min(len(bi), len(bj))):
        if bi[k] != bj[k]:
            break
        else:
            k += 1
    print(len(bi) - k + len(bj) - k)
