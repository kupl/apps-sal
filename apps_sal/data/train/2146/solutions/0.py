import sys
readline = sys.stdin.readline
(N, D, M) = map(int, readline().split())
A = list(map(int, readline().split()))
Am = [a for a in A if a > M]
Ao = [a for a in A if a <= M]
Am.sort(reverse=True)
Ao.sort(reverse=True)
Cam = Am[:]
Cao = Ao[:]
for i in range(1, len(Cam)):
    Cam[i] += Cam[i - 1]
for i in range(1, len(Cao)):
    Cao[i] += Cao[i - 1]
k = -(-N // (D + 1))
ans = sum(Am[:k])
lcam = len(Cam)
Cam = [0] + Cam
for i in range(len(Cao)):
    k = min(lcam, -(-(N - (i + 1)) // (D + 1)))
    ans = max(ans, Cao[i] + Cam[k])
print(ans)
