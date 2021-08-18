N, M = list(map(int, input().split()))
for i in range(1, N, 2):
    print(((i * ".|.").center(3 * N, "-")))
print(("-WELCOME-".center(3 * N, "-")))
for i in range(N - 2, -1, -2):
    print(((i * ".|.").center(3 * N, "-")))
