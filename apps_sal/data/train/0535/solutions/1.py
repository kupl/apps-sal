
def solve(N, M, x, y):
    n, m = min(N, M), max(N, M)

    count = ((n - 1) * n * (2 * n - 1) // 3 + (m - n + 1) * n**2) * 2  # total sum of l_d and         r_d at all places
    p1, p2 = min(x - 1, y - 1), min(N - x, M - y)
    r1, r2 = min(M - y, x - 1), min(N - x, y - 1)
    # print('-->',p1,p2,r1,r2)
    count += (n + m) * n * m  # total sum of places queen 2 cannt have at all cells         including kings cell
    # print('1',count)

    count -= p1 + p2 + r1 + r2 + n + m + 2  # place occupied by king cannot be         occupied by queen
    # print('2',count)

    count += (n * m) - (p1 + p2 + r1 + r2 + n + m - 1)  # total count where queen 2 cannot         come
    # print('3',count)

    count -= (n * m - 1) * 3  # total count where queen 2 cannot come where centre is         counted once
    # print('4',count)
    tot = (n * m - 1) * n * m - count
    # print(tot)
    tot += 2 * (p1 * p2 + r1 * r2 + (x - 1) * (N - x) + (y - 1) * (M - y))

    return tot


for _ in range(int(input())):

    n, m, x, y = list(map(int, input().split()))
    print(solve(n, m, x, y))
