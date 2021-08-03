def subsetsum(array, g):

    if g == 0 or g < 1:
        return False
    elif len(array) == 0:
        return False
    else:
        if array[0] == g:
            return True
        else:
            return subsetsum(array[1:], (g - array[0])) or subsetsum(array[1:], g)


n, q = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
for qq in range(q):
    x = [i for i in input().split()]
    a = int(x[0])
    if a == 1:
        w[int(x[1]) - 1] = int(x[2])
    elif a == 2:
        l = int(x[1]) - 1
        r = int(x[2]) - 1
        w = w[:l] + w[r:l - 1:-1] + w[r + 1:]
    else:
        l = int(x[1]) - 1
        r = int(x[2])
        if subsetsum(w[l:r], int(x[3])):
            print("Yes")
        else:
            print("No")
