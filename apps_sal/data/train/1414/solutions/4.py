def read():
    return list(map(int, input().split()))


def read_s():
    return list(map(str, input().split()))


def found(K, gender, L, R):
    ans = []
    for i in range(K):
        ans.append(gender * K)
    for i in range(L - K + 1):
        for j in range(R - K + 1):
            Query_list = []
            for qq in range(K):
                Query_list.append(grid[i + qq][j:j + K])
            if Query_list == ans:
                return True
    return False


(L, R, Q) = read()
grid = []
for i in range(L):
    grid.append(str(input()))
for i in range(Q):
    (K, gender) = input().split()
    (K, gender) = (int(K), str(gender))
    print('yes' if found(K, gender, L, R) else 'no')
