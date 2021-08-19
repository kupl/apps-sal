def func():
    count = 0
    N = len(A)
    for i in range(N - 1):
        marker = [0 for h in range(N)]
        for group_size in range(1, N - i):
            I = set(A[i:i + group_size])
            m = 0
            new_element = A[i + group_size - 1]
            for j in range(i + group_size, N):
                if group_size == 1:
                    if A[j] not in I:
                        m += 1
                    else:
                        marker[j] = 1
                        count += m * (m + 1) / 2
                        m = 0
                elif marker[j] == 0 and A[j] != new_element:
                    m += 1
                else:
                    marker[j] = 1
                    count += m * (m + 1) / 2
                    m = 0
            count += m * (m + 1) / 2
    print(count)


T = int(input())
for t in range(T):
    N = int(input())
    A = input().split(' ')
    for i in range(N):
        A[i] = int(A[i])
    func()
