def func():
    count = 0
    for i in range(N - 1):
        for group_size in range(1, N - i):
            I = set(A[i:i + group_size])
            m = 0
            for j in range(i + group_size, N):
                if A[j] not in I:
                    m += 1
                else:
                    count += m * (m + 1) / 2
                    m = 0
            count += m * (m + 1) / 2
    print(count)


T = int(input())
for t in range(T):
    N = int(input())
    A = input().split(' ')
    func()
