n = int(input())
arr = list(map(int, input().split()))
for i in arr:
    if i == 2:
        print("1", end=" ")
    else:
        print(i ^ 2, end=" ")
