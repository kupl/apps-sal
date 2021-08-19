def cows(lst):
    (k1, k2) = (0, 0)
    for i in range(len(lst)):
        if lst[i] == 1:
            k1 += 1
        else:
            k2 += k1
    return k2


n = int(input())
a = [int(j) for j in input().split()]
print(cows(a))
