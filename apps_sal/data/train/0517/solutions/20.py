# cook your dish here

N, M = map(int, input().split())

pow2ModM = [1 for i in range(N + 1)]
pow2ModM[0] = 1
for i in range(1, N + 1):
    pow2ModM[i] = (pow2ModM[i - 1] * 2) % M


def fModM(N):
    answer = pow2ModM[N]
    for d in range(1, N):
        if N % d == 0:
            answer = (answer - fModM(d)) % M
    return answer


print(fModM(N))
