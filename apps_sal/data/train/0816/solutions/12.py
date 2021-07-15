M = int(input())
arr = list(map(int,input().split()))
N = int(input())
ans = []
for i in range(N):
    a = int(input())
    ans.append(arr[a-1])
    arr.pop(a-1)
for i in ans:
    print(i)

