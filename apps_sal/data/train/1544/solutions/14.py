for tc in range(int(input())):
    K = int(input())
    for i in range(K):
        ar = []
        for j in range(i + 1):
            if i == K - 1 or j == 0 or j == i:
                ar.append('*')
            else:
                ar.append(' ')
        print(''.join(ar))
