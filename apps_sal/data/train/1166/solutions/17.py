# cook your dish here
input()

arr = list(map(int, input().split()))

Q = int(input())

for item in range(Q):
    K = int(input())
    
    total = 0
    for i in range(len(arr)):
        hasK = False
        if arr[i] >= K:
            if arr[i] == K:
                hasK = True
                total += 1
            j = i + 1
            while j < len(arr) and arr[j] >= K:
                if arr[j] == K:
                    hasK = True
                if hasK:
                    total += 1
                j += 1
                    
    print(total)
