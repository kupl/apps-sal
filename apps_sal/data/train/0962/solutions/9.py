for tc in range(int(input())):
    K = int(input())
    A = []
    for i in range(K):
        ar = [str(_ + 1) for _ in range(i + 1)]
        if i % 2:
            ar = ar[::-1]
        A.append(ar)
    A = A[::-1]
    for row in A:
        print(''.join(row))
