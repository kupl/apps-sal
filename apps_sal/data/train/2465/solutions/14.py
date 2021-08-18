def doS(N, arr):
    if (N == 1):
        return False

    if not(arr[N] == None):
        return arr[N]

    for i in range(1, N):
        if(N % i == 0):
            if not doS(N - i, arr):
                arr[i] = True
                return True

    arr[N] = False
    return False


class Solution:
    def divisorGame(self, N: int) -> bool:

        arr = [None] * (N + 1)
        print(arr)
        return doS(N, arr)
