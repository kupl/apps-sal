for _ in range(int(input())):
    K = int(input())
    arr = list(map(int, input().split()))
    P = []
    for i in range(K):
        for j in range(i + 1, K):
            P.append(arr[i] + arr[j])
    print(P.count(max(P)) / len(P))
