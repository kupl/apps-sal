
for test_case in range(int(input())):
    S = str(input())
    N = len(S)
    A = [0] * 27
    for character in S:
        A[ord(character) - 65] = A[ord(character) - 65] + 1
    A.sort(reverse=True)
    minSwap = N
    for i in range(1, 27):
        if N % i == 0:
            temp = N // i
            tempSwap = 0
            for f in range(i):
                if temp > A[f]:
                    tempSwap = tempSwap + temp - A[f]
            if tempSwap <= minSwap:
                minSwap = tempSwap
    if minSwap == N + 1:
        minSwap = 0
    print(minSwap)
