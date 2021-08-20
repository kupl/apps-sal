for _ in range(int(input())):
    (A, B) = list(map(int, input().split()))
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    for i in range(A * B):
        if l1[i] < l2[i]:
            l1[i] = 0
        else:
            l2[i] = 0
    l1.sort(reverse=True)
    l2.sort(reverse=True)
    (w, d, c) = (0, 0, 0)
    for j in range(A):
        if l1[c] > l2[d]:
            w += 1
            c += 1
            d += B - 1
        else:
            d += B
    print(w)
