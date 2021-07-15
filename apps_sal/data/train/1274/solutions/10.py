for tc in range(int(input())):
    K = int(input())
    for i in range(K):
        ar = [str(i + 1 if j % 2 else j + 2 >> 1) for j in range(2 * K)]
        print(''.join(ar))
