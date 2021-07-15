T = int(input())
for _ in range(T):
    N, K1, K2 = list(map(int, input().split()))
    P1, P2, P3, P4 = list(map(int, input().split()))
    ans = 0
    arr = [0] * (1005)

    length = len(arr)
    for i in range(1,N+1):

        j = 0
        while j < length:
            arr[j] += 1
            j += i

    for i in range(K1,K2+1):
        if arr[i]==3:
           ans += P1
        elif arr[i]%2==1:
            ans += P2
        else:
            ans += P3

    print(ans)

