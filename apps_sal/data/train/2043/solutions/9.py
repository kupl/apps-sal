n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
start = []
end = []
for i in range(n):
    if A[i][0] == 0:
        start.append(i)
    elif A[i][1] == 0:
        end.append(i)
for curr in range(len(start)):
    x = start[curr]
    while A[x][1] != 0:
        x = A[x][1] - 1
    if curr != len(start) - 1:
        A[x][1] = start[curr + 1] + 1
        A[A[x][1] - 1][0] = x + 1
for i in range(n):
    print(A[i][0], A[i][1])
