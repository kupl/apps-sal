from bisect import bisect_left, bisect_right

N = int(input())
xs = list(map(int, input().split()))
L = int(input())
Q = int(input())
ABs = [tuple([int(x)-1 for x in input().split()]) for _ in range(Q)]

logN = ((N-1).bit_length())
parentss = [[N-1]*(logN+1) for _ in range(N)]
for i in range(N-1):
    iL = bisect_right(xs, xs[i]+L)
    parentss[i][0] = iL-1

for d in range(1, logN+1):
    for i in range(N-1):
        parentss[i][d] = parentss[parentss[i][d-1]][d-1]

anss = []
for A, B in ABs:
    if A > B:
        A, B = B, A
    i = A
    ans = 1
    for d in reversed(list(range(logN+1))):
        if parentss[i][d] < B:
            i = parentss[i][d]
            ans += 2**d
    anss.append(ans)

print(('\n'.join(map(str, anss))))

