for tc in range(int(input())):
    K = int(input())
    k = 1
    for i in range(K):
        ar = []
        for j in range(i + 1):
            ar.append(str(k))
            k += 1
        print(''.join(ar[::-1]))
