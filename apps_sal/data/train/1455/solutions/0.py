n = eval(input())
grades = list(map(int, input().split()))
m = eval(input())
for df in range(m):
    x, y = list(map(int, input().split()))
    arr = []
    arr = grades[x - 1:y]
    arr.sort()
    sum = 0
    # arr.append(1000000)
    for nh in range(0, len(arr) - 1, 1):
        sum = sum + (arr[nh + 1] - arr[nh])**2
        # print sum,len(arr),nh+1,nh
    print(sum)
