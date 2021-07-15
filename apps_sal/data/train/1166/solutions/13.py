N = int(input())
array = list(map(int, input().split()))
for _ in range(int(input())):
    K = int(input())
    count = 0
    for i in range(N):
        for j in range(i+1,N+1):
            if K == min(array[i:j]):
                count += 1
    print(count)
