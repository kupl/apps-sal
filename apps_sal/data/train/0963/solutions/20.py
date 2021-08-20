def find_max(A, s, e):
    m = 0
    m_index = s
    for i in range(s, e + 1):
        if A[i] > m:
            m = A[i]
            m_index = i
    return m_index


def solution(A, s, e, ans):
    m_index = find_max(A, s, e)
    if m_index == s or m_index == e:
        ans = ans + 1
        return ans
    return min(solution(A, m_index + 1, e, ans + 1), solution(A, s, m_index - 1, ans + 1))


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = solution(A, 0, N - 1, 0)
    print(ans)
