M = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(int(input())):
    a = int(input())
    ans.append(arr[a - 1])
    arr.pop(a - 1)
for i in ans:
    print(i)
