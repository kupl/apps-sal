t = int(input())


def maxsa(A):
    ans = 0
    # print("asdasd")
    for i in range(n):
        cur_maxx = 0
        for j in range(4):
            cur_maxx = max(cur_maxx, A[j][i])
        ans += cur_maxx
    return ans


def fu(A):
    answer = 0
    for j in range(n):
        A[0] = A[0][1:] + A[0][:1]
        for i in range(n):
            A[1] = A[1][1:] + A[1][:1]
            for k in range(n):
                A[2] = A[2][1:] + A[2][:1]
                for l in range(n):
                    A[3] = A[3][1:] + A[3][:1]
                    # print(A)
                    cur_ans = maxsa(A)
                    answer = max(answer, cur_ans)
    return answer


for j in range(t):
    n, m = map(int, input().split())
    A = [0] * n
    inds = [-1, -1, -1, -1]
    maxs = [0, 0, 0, 0]
    for j in range(n):
        A[j] = list(map(int, input().split()))
    for j in range(m):
        cur_maxs = 0
        for i in range(n):
            cur_maxs = max(cur_maxs, A[i][j])
        maxs.append(cur_maxs)
        inds.append(j)
        ind = 4
        # print(cur_maxs)
        while ind != 0 and maxs[ind] > maxs[ind - 1]:
            inds[ind], inds[ind - 1] = inds[ind - 1], inds[ind]
            maxs[ind], maxs[ind - 1] = maxs[ind - 1], maxs[ind]
            ind -= 1
        maxs.pop()
        inds.pop()

    # print(maxs)
    # print(inds)
    S = [0] * 4
    for j in range(4):
        if inds[j] != -1:
            # print(A)
            # print(inds[j])
            S[j] = [s[inds[j]] for s in A]
            # print(S[j])
        else:
            S[j] = [0] * n
    # print(S)
    print(fu(S))
